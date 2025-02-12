from rest_framework import serializers

from exams.models import StudentAnswer, TestResult, TestSession
from quizzes.models import Choice, Question


class ExamChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text"]


class ExamQuestionSerializer(serializers.ModelSerializer):
    choices = ExamChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "choices"]


class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ["question", "selected_choice"]

    def create(self, validated_data):
        session = self.context["session"]
        return StudentAnswer.objects.create(session=session, **validated_data)


class StudentAnswerListSerializer(serializers.Serializer):
    answers = StudentAnswerSerializer(many=True)

    def create(self, validated_data):
        session = self.context["session"]
        answers_data = validated_data["answers"]

        student_answers = [
            StudentAnswer(session=session, **answer) for answer in answers_data
        ]
        StudentAnswer.objects.bulk_create(student_answers)

        return {"answers": student_answers}


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ["id", "correct_answers", "incorrect_answers", "total_score"]


class TestSessionSerializer(serializers.ModelSerializer):
    result = TestResultSerializer(read_only=True)

    class Meta:
        model = TestSession
        fields = ["id", "student", "quiz", "started_at", "completed_at", "is_completed", "score", "result"]


class LeaderboardSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.username", read_only=True)
    correct_answers = serializers.IntegerField(source="result.correct_answers", read_only=True)
    incorrect_answers = serializers.IntegerField(source="result,incorrect_answers", read_only=True)

    class Meta:
        model = TestSession
        fields = ["id", "student_id", "student_name", "score", "correct_answers", "incorrect_answers"]