from rest_framework import status, generics
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.permissions import IsTeacher
from quizzes.models import Quiz, Question, Choice
from quizzes.permissions import IsCreatorOfQuiz, IsQuizOwner
from quizzes.serializers import CreateQuizSerializer, QuizzesListSerializer, QuestionSerializer, \
    UpdateQuestionSerializer, ChoiceSerializer, ChoiceCreateSerializer


class TeacherQuizzesListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer_class = QuizzesListSerializer

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

class QuizDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsCreatorOfQuiz]
    serializer_class = QuizzesListSerializer
    queryset = Quiz.objects.all()
    lookup_field = "pk"



class QuizQuestionsListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs.get("quiz_id"))
        return quiz.questions.all()


class CreateQuestionAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer_class = QuestionSerializer

    def post(self, request):
        serializer = QuestionSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Savol qo'shildi",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsQuizOwner]
    queryset = Question.objects.all()
    serializer_class = UpdateQuestionSerializer
    lookup_field = "pk"


class QuestionChoicesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChoiceSerializer

    def get(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            serializer = ChoiceSerializer(question.choices.all(), many=True)
            data = {
                "Question": question.text,
                "Variants": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Question.DoesNotExist:
            return Response(data={"message": "Bunday id li savol mavjud emas"}, status=status.HTTP_400_BAD_REQUEST)


class ChoiceCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ChoiceCreateSerializer
    queryset = Choice.objects.all()

class ChoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    lookup_field = "pk"

