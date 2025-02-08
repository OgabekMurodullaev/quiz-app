from django.urls import path

from exams.views import QuizQuestionsListAPIView, SubmitStudentAnswersAPIView

urlpatterns = [
    path("<int:quiz_id>/questions/", QuizQuestionsListAPIView.as_view()),
    path("<int:quiz_id>/submit/", SubmitStudentAnswersAPIView.as_view()),
]