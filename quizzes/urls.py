from django.urls import path

from quizzes.views import (CreateQuizAPIView, TeacherQuizzesListAPIView, QuizDetailAPIView, QuizUpdateAPIVew, \
                           QuizDeleteAPIView, CreateQuestionAPIView, QuestionRetrieveUpdateView,
                           QuizQuestionsListAPIView, ChoiceRetrieveUpdateDestroyView, ChoiceCreateView,
                           QuestionChoicesAPIView)

urlpatterns = [
    path('create/', CreateQuizAPIView.as_view()),
    path('my-quizzes/', TeacherQuizzesListAPIView.as_view()),
    path('<int:pk>/', QuizDetailAPIView.as_view()),
    path('<int:pk>/update/', QuizUpdateAPIVew.as_view()),
    path('<int:pk>/delete/', QuizDeleteAPIView.as_view()),

    path('tests/<int:quiz_id>/', QuizQuestionsListAPIView.as_view()),
    path('tests/create/', CreateQuestionAPIView.as_view()),
    path('tests/<int:pk>/', QuestionRetrieveUpdateView.as_view()),

    path('choices/<int:question_id>/', QuestionChoicesAPIView.as_view()),
    path('choices/create/', ChoiceCreateView.as_view()),
    path('choices/<int:pk>/', ChoiceRetrieveUpdateDestroyView.as_view()),
]