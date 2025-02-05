from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.models import Group
from groups.serializers import GroupSerializer


class GroupInfoAPIView(APIView):
    serializer_class = GroupSerializer

    def get(self, request, class_id):
        obj = get_object_or_404(Group, id=class_id)
        serializer = GroupSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
