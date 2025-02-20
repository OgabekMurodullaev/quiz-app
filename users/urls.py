from django.urls import path

from .views import UserRegisterAPIView, UserLoginAPIView, UserProfileView, CustomTokenRefreshView

urlpatterns = [
    path('signup/', UserRegisterAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
]