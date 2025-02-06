from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsCreatorOfQuiz(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.teacher == request.user:
            return True
        raise PermissionDenied(f"Siz bu testning egasi emassiz va testni yangilay olmaysiz!")