from rest_framework import serializers

from groups.models import Group
from quizzes.models import Quiz


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
