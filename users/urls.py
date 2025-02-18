from django.urls import path
from .views import UserRegisterAPIView, UserLoginAPIView, RefreshTokenView, UserProfileView

urlpatterns = [
    path('signup/', UserRegisterAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view()),
]