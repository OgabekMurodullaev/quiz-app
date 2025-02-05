from rest_framework import serializers

from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField("get_students_count")

    class Meta:
        model = Group
        fields = ("name", "teacher", "students_count")

    def get_students_count(self, obj):
        return obj.student.count()
