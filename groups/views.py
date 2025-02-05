from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.models import Group
from groups.permissions import IsTeacher, IsOwnerOfGroup
from groups.serializers import GroupSerializer, CreateGroupSerializer, AddStudentToGroupSerializer
from users.models import User


class GroupInfoAPIView(APIView):
    serializer_class = GroupSerializer

    def get(self, request, group_id):
        obj = get_object_or_404(Group, id=group_id)
        serializer = GroupSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupCreateAPIView(APIView):
    serializer_class = CreateGroupSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def post(self, request):
        serializer = CreateGroupSerializer(data=request.data)
        if serializer.is_valid():
            group_name = serializer.validated_data["name"]
            student_ids = serializer.validated_data["students_ids"]

            group = Group.objects.create(name=group_name, teacher=request.user)

            for student_id in student_ids:
                student = User.objects.get(id=student_id)
                group.student.add(student)

            group.save()

            data = {
                "message": "Group created successfully",
                "data": serializer.data
            }

            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddStudentToGroupAPIView(APIView):
    permission_classes = [IsOwnerOfGroup]
    serializer_class = AddStudentToGroupSerializer

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)

        self.check_object_permissions(request, group)

        serializer = AddStudentToGroupSerializer(data=request.data)
        if serializer.is_valid():
            group.student.add(*serializer.validated_data['students'])
            return Response({"detail": "O'quvchilar guruhga qo'shildi!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

