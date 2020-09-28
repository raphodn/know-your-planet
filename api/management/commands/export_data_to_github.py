from datetime import datetime

# from django.conf import settings
from django.core.management import BaseCommand

from api import utilities, utilities_github


class Command(BaseCommand):
    """
    Usage:
    python manage.py export_data_to_github

    TODO:
    - commit multiple files at once ? https://github.com/PyGithub/PyGithub/issues/1628
    """

    def handle(self, *args, **options):
        # init
        current_datetime = datetime.now()
        current_datetime_string = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")
        current_datetime_string_pretty = current_datetime.strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # YYYY-MM-DD HH:MM:SS
        current_date_string = current_datetime.strftime("%Y-%m-%d")  # YYYY-MM-DD
        data_update_branch_name = f"data-update-{current_datetime_string}"
        data_update_pull_request_name = f"Data: update ({current_date_string})"

        # create branch
        utilities_github.create_branch(data_update_branch_name)

        # update & commit data files
        # data/questions.yaml
        # data/quizzes.yaml
        # data/tags.yaml
        questions_yaml = utilities.serialize_model_to_yaml(model_label="question")
        utilities_github.create_file(
            file_path="data/questions.yaml",
            commit_message="update questions",
            file_content=questions_yaml,
            branch_name=data_update_branch_name,
        )
        quizzes_yaml = utilities.serialize_model_to_yaml(model_label="quiz")
        utilities_github.create_file(
            file_path="data/quizzes.yaml",
            commit_message="update quizzes",
            file_content=quizzes_yaml,
            branch_name=data_update_branch_name,
        )
        tags_yaml = utilities.serialize_model_to_yaml(model_label="tag")
        utilities_github.create_file(
            file_path="data/tags.yaml",
            commit_message="update tags",
            file_content=tags_yaml,
            branch_name=data_update_branch_name,
        )

        # update & commit frontend file
        # frontend/src/constants.js
        old_frontend_constants_file_content = utilities_github.get_file(
            file_path="frontend/src/constants.js", branch_name=data_update_branch_name
        )
        new_frontend_constants_file_content_string = utilities.update_frontend_last_updated_datetime(  # noqa
            old_frontend_constants_file_content.decoded_content.decode(),
            current_datetime_string_pretty,
        )
        utilities_github.update_file(
            file_path="frontend/src/constants.js",
            commit_message="update frontend constants (last_updated datetime)",
            file_content=new_frontend_constants_file_content_string,
            branch_name=data_update_branch_name,
        )

        # create pull request
        pull_request = utilities_github.create_pull_request(
            pull_request_title=data_update_pull_request_name,
            pull_request_message="Mise à jour de la donnée : <ul><li>data/questions.yaml</li><li>data/quizzes.yaml</li><li>data/tags.yaml</li></ul>",  # noqa
            branch_name=data_update_branch_name,
        )
        print(pull_request.html_url)

        # return
        self.stdout.write(pull_request.html_url)