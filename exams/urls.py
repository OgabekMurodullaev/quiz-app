from django.urls import path

from exams.views import QuizQuestionsListAPIView, SubmitStudentAnswersAPIView, TestSessionResultAPIView, LeaderBoardAPIView

urlpatterns = [
    path("<int:quiz_id>/questions/", QuizQuestionsListAPIView.as_view()),
    path("<int:quiz_id>/submit/", SubmitStudentAnswersAPIView.as_view()),
    path("<int:quiz_id>/result/<int:student_id>/", TestSessionResultAPIView.as_view()),
    path("<int:quiz_id>/leaderboard/", LeaderBoardAPIView.as_view()),
]