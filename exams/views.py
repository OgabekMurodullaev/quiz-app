from venv import create

from django.db import transaction
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from exams.models import TestSession
from exams.serializers import QuestionSerializer, StudentAnswerSerializer, StudentAnswerListSerializer
from quizzes.models import Question, Quiz


class QuizQuestionsListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)

        if not quiz.groups.filter(student=request.user).exists():
            return Response(
                {"detail": "Sizga bu testni ishlash uchun ruxsat yo'q."},
                status=status.HTTP_403_FORBIDDEN
            )

        questions = quiz.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        data = {
            "detail": f"{quiz.name} - {quiz.teacher}",
            "questions": serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)


class SubmitStudentAnswersAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = StudentAnswerListSerializer

    def post(self, request, quiz_id):
        user = request.user
        quiz = get_object_or_404(Quiz, id=quiz_id)

        if not quiz.groups.filter(student=user).exists():
            return Response(
                {"detail": "Siz bu test savollariga javob bera olmaysiz"},
                status=status.HTTP_403_FORBIDDEN
            )

        session, created = TestSession.objects.get_or_create(student=user, quiz=quiz)

        answers_data = request.data.get("answers", [])

        if not answers_data:
            return Response({"detail": "Javoblar bo'sh bo'lishi mumkin emas!"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            serializer = StudentAnswerSerializer(
                data=answers_data, many=True, context={"request": request, "session": session}
            )
            if serializer.is_valid():
                serializer.save()  # ✅ commit() shart emas, Django avtomatik commit qiladi
                return Response({"detail": "Javoblar saqlandi."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
