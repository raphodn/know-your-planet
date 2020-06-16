<template>
  <section class="card-feedback small">
    <div class="row margin-top-bottom-10">
      <h3 class="margin-5">Votre avis sur {{ (context.source) === 'question' ? 'cette' : 'ce' }} {{ context.source }} ?</h3>
      <!-- Option to hide card ? -->

      <div>
        <button v-if="!feedbackSubmitted" class="btn btn-sm btn-primary-light margin-left-right-10 small" title="J'ai aimé" @click="submitFeedback('like')" :disabled="feedbackSubmitted">👍<span class="fake-link"></span></button>
        <button v-if="!feedbackSubmitted" class="btn btn-sm btn-primary-light margin-left-right-10 small" title="Je n'ai pas aimé" @click="submitFeedback('dislike')" :disabled="feedbackSubmitted">👎<span class="fake-link"></span></button>
        <span v-if="feedbackSubmitted" class="margin-left-right-10">Merci 💯</span>
        <button class="btn btn-sm btn-primary-light margin-left-right-10 small" title="Votre avis" @click="showContributionForm = true">💬&nbsp;<span class="fake-link">Suggérer une modification</span></button>
      </div>
    </div>

    <!-- Contribution form -->
    <template v-if="showContributionForm">
      <hr class="custom-separator" />
      <form @submit.prevent="submitContribution" v-if="!contributionSubmitted">
        <h3 class="margin-bottom-0">
          <label for="contribution_text">Votre suggestion, commentaire, ... <span class="color-red">*</span></label>
        </h3>
        <p v-if="(context.source) === 'question' && (!context.item.answer_explanation || !context.item.answer_accessible_url || !context.item.answer_image_url)">
          <i>(donnée(s) manquante à cette question: <span v-if="!context.item.answer_explanation">une explication, </span><span v-if="!context.item.answer_accessible_url">un lien, </span><span v-if="!context.item.answer_image_url">une image</span>)</i>
        </p>
        <div class="row">
          <div class="col">
            <textarea id="contribution_text" class="form-control" rows="2" v-model="contribution_text" required></textarea>
            <p>
              <button type="submit" class="btn btn-sm" :class="contribution_text ? 'btn-primary' : 'btn-outline-primary'" :disabled="!contribution_text">📩&nbsp;Envoyer !</button>
            </p>
          </div>
        </div>
      </form>
      <div v-if="contributionSubmitted && loading" class="loading">
        <p>Envoi de votre suggestion...</p>
      </div>

      <div v-if="contributionSubmitted && error" class="error">
        <h3>Il y a eu une erreur 😢</h3>
        <p>{{ error }}</p>
      </div>

      <div v-if="contributionSubmitted && contributionResponse">
        <h3>Merci beaucoup 💯</h3>
        <p>On fera de notre mieux pour prendre en compte votre suggestion.</p>
      </div>
    </template>

  </section>
</template>

<script>
export default {
  name: 'FeedbackCard',
  props: {
    context: Object
  },

  data() {
    return {
      contribution_text: "",
      showContributionForm: false,
      feedbackSubmitted: false,
      contributionSubmitted: false,
      contributionResponse: null,
      loading: false,
      error: null,
    }
  },

  methods: {
    submitFeedback(feedback_choice) {
      this.feedbackSubmitted = feedback_choice;
      this.error = null;
      this.loading = true;
      fetch(`${process.env.VUE_APP_API_ENDPOINT}/${(this.context.source === 'question') ? 'questions' : 'quizzes'}/${this.context.item.id}/feedback-events`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          choice: feedback_choice,
          source: this.context.source // only for 'questions'
        })
      })
      .then(response => {
        return response.json()
      })
      // eslint-disable-next-line
      .then(data => {
        // console.log(data);
      })
      .catch(error => {
        console.log(error)
      })
    },
    submitContribution() {
      this.contributionSubmitted = true;
      this.error = this.contributionResponse = null;
      this.loading = true;
      fetch(`${process.env.VUE_APP_API_ENDPOINT}/contribute`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: this.contribution_text,
          description: (this.context.source === 'question') ? `Question #${this.context.item.id} - ${this.context.item.category} - ${this.context.item.text}` : `Quiz #${this.context.item.id} - ${this.context.item.name}`,
          type: `commentaire ${this.context.source}`
        })
      })
      .then(response => {
        this.loading = false
        return response.json()
      })
      .then(data => {
        this.contributionResponse = data;
      })
      .catch(error => {
        console.log(error)
        this.error = error;
      })
    }
  }
}
</script>

<style scoped>
.card-feedback {
  border: 1px solid var(--primary);
  border-radius: 5px;
  margin: 10px 0px;
  background-color: #F8F8F8;
}

.btn-feedback {
  margin: 0;
  padding: 0;
  font-size: small;
}
</style>