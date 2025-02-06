from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.permissions import IsTeacher
from quizzes.models import Quiz
from quizzes.permissions import IsCreatorOfQuiz
from quizzes.serializers import CreateQuizSerializer, QuizzesListSerializer


class TeacherQuizzesListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer = QuizzesListSerializer

    def get(self, request):
        teacher = request.user
        quizzes = Quiz.objects.filter(teacher=teacher)
        if quizzes:
            serializer = QuizzesListSerializer(quizzes, many=True)
            data = {
                "message": "Siz yaratgan quizlar ro'yxatdi",
                "data": serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response({"message": "Sizda hech qanday quizlar yo'q"}, status=status.HTTP_400_BAD_REQUEST)


class CreateQuizAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer_class = CreateQuizSerializer

    def post(self, request):
        serializer = CreateQuizSerializer(data=request.data, context={'request': request})
        teacher = request.user

        if serializer.is_valid():
            name = serializer.validated_data['name']
            description = serializer.validated_data['description']
            groups = serializer.validated_data['groups']

            quiz = Quiz.objects.create(teacher=teacher, name=name, description=description)
            quiz.groups.set(serializer.validated_data['groups'])

            data = {
                "message": f"{name} quizi muvaffaqiyatli yaratildi!",
                "data": serializer.data
            }

            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizzesListSerializer
    queryset = Quiz.objects.all()
    lookup_field = "pk"


class QuizUpdateAPIVew(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsCreatorOfQuiz]
    serializer_class = QuizzesListSerializer
    queryset = Quiz.objects.all()
    lookup_field = "pk"


