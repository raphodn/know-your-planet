from django.test import TestCase

from api.models import Category, Tag, Question, Quiz


class FixturesTest(TestCase):
    fixtures = [
        "data/categories.yaml",
        "data/tags.yaml",
        "data/questions.yaml",
        "data/quizzes.yaml",
    ]

    def test_fixtures_load_successfully(self):
        self.assertTrue(Category.objects.count())
        self.assertTrue(Tag.objects.count())
        self.assertTrue(Question.objects.count())
        self.assertTrue(Quiz.objects.count())