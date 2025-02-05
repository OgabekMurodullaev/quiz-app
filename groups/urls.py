from linecache import clearcache

from django.urls import path
from .views import GroupInfoAPIView, GroupCreateAPIView, AddStudentToGroupAPIView

urlpatterns = [
    path('create/', GroupCreateAPIView.as_view()),

    path('<int:group_id>/info/', GroupInfoAPIView.as_view()),
    path('<int:group_id>/add-students/', AddStudentToGroupAPIView.as_view()),

]
