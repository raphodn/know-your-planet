from django.core.management import BaseCommand

from api.models import Quiz  # , Question, QuizQuestion


class Command(BaseCommand):
    """
    Usage:
    - python manage.py sanitize_quiz_question_ordering
    - python manage.py sanitize_quiz_question_ordering --fix
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-input",
            default=False,
            action="store_true",
            dest="sanitize",
            help="Fix ordering errors",
        )

    def handle(self, *args, **kwargs):
        for quiz in Quiz.objects.all():
            print("-----")
            print(quiz.id, quiz.name)
            for index, qq in enumerate(quiz.quizquestion_set.all()):
                order_correct = qq.order == index + 1
                print(qq.order, order_correct, qq.question.id)
                if not order_correct:
                    print(">>> do something with above")


"""
TODO :
- reset db + add superuser to reset script
- add order errors
- make sure the command detects them
- implement fix option
"""
