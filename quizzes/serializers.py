from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from groups.models import Group
from quizzes.models import Quiz, Choice, Question


class QuizzesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        exclude = ["teacher"]


class CreateQuizSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.context)
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            self.fields['groups'].queryset = Group.objects.filter(teacher=request.user)
           

    def validate_groups(self, groups):
        user = self.context['request'].user
        valid_groups = Group.objects.filter(teacher=user)

        for group in groups:
            if group not in valid_groups:
                raise serializers.ValidationError(f"{group.name} guruhi sizga tegishli emas!")

        return groups


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text", "is_correct"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())

    class Meta:
        model = Question
        fields = ["quiz", "text", "choices"]

    def validate_quiz(self, value):
        quiz = Quiz.objects.filter(id=value.id).first()
        if quiz is None:
            raise ValidationError(f"{quiz} idli quiz topilmadi!")

        if quiz and quiz.teacher != self.context['request'].user:
            raise ValidationError("Kechirasiz siz bu Quizga savol qo'shish imkoniyatiga ega emassiz")

        return value

    def create(self, validated_data):
        choices_data = validated_data.pop("choices")
        question = Question.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(question=question, text=choice_data["text"], is_correct=choice_data["is_correct"])

        return question