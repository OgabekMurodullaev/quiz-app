from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from groups.models import Group
from users.models import User


class GroupSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField("get_students_count")

    class Meta:
        model = Group
        fields = ("name", "teacher", "students_count")

    def get_students_count(self, obj) -> int:
        return obj.student.count()


class CreateGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    students_ids = serializers.ListField(child=serializers.IntegerField(), required=False)


    def validate_student_ids(self, value):
        for student_id in value:
            try:
                student = User.objects.get(id=student_id)
                if student.user_type == 'teacher':
                    raise ValidationError(f"ID {student_id} noto'g'ri. Faqat talaba id kiritilishi kerak")

            except User.DoesNotExist as e:
                raise ValidationError(f"ID {student_id} topilmadi.")

        return value


class AddStudentToGroupSerializer(serializers.Serializer):
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(user_type='student'), many=True)

