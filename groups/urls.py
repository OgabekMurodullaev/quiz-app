from django.urls import path
from .views import GroupInfoAPIView

urlpatterns = [
    path('<int:class_id>/info/', GroupInfoAPIView.as_view()),
]
