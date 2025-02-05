from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.user_type == 'teacher':
            return True
        raise PermissionDenied("Kechirasiz, siz guruh yaratish imkoniyatiga ega emassiz!")


class IsOwnerOfGroup(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.teacher == request.user:
            return True
        raise PermissionDenied("Siz faqatgina o'z guruh(lar)ingizga a'zo qo'sha olasiz.")

