from rest_framework import serializers

from exams.models import StudentAnswer, TestResult, TestSession
from quizzes.models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "choices"]


class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ["question", "selected_choice"]

    def create(self, validated_data):
        return StudentAnswer.objects.create(**validated_data)


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ["id", "correct_answers", "incorrect_answers", "total_score"]


class TestSessionSerializer(serializers.ModelSerializer):
    result = TestResultSerializer(read_only=True)

    class Meta:
        model = TestSession
        fields = ["id", "quiz", "started_at", "completed_at", "is_completed", "score", "result"]
