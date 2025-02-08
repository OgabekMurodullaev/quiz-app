from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from exams.models import StudentAnswer, TestResult

@receiver(post_save, sender=StudentAnswer)
def create_or_update_test_result(sender, instance, **kwargs):
    transaction.on_commit(lambda: process_test_result(instance))  # ✅ Transaction tugagandan keyin signal chaqiriladi

def process_test_result(instance):
    session = instance.session

    if session.answers.count() == session.quiz.questions.count():
        session.is_completed = True
        session.completed_at = instance.answered_at
        session.save()

        test_result, created = TestResult.objects.get_or_create(session=session)
        test_result.correct_answers = session.answers.filter(is_correct=True).count()
        test_result.incorrect_answers = session.answers.filter(is_correct=False).count()
        test_result.total_score = (test_result.correct_answers / session.quiz.questions.count()) * 100
        test_result.save()

        print(f"✅ TestResult saqlandi! ID: {test_result.id}, Score: {test_result.total_score}%")
