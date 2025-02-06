from django.urls import path

from quizzes.views import CreateQuizAPIView, TeacherQuizzesListAPIView, QuizDetailAPIView, QuizUpdateAPIVew

urlpatterns = [
    path('create/', CreateQuizAPIView.as_view()),
    path('my-quizzes/', TeacherQuizzesListAPIView.as_view()),
    path('<int:pk>/', QuizDetailAPIView.as_view()),
    path('<int:pk>/update/', QuizUpdateAPIVew.as_view()),
]