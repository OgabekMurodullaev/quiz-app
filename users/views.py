from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .filters import StudentFilter
from .models import User
from .serializers import UserRegisterSerializer, LoginSerializer, TokenRefreshSerializer, UserSerializer


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "message": "You have successfully register",
                "data": serializer.data
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                data = {
                    "message": "You have successfully logged in",
                    "access": access_token,
                    "refresh": str(refresh)
                }
                return Response(data=data, status=status.HTTP_200_OK)
            return Response(data={"data": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

class UserProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user

        user_data = {
            "id": user.id,
            "username": user.username,
            "user_type": user.user_type
        }

        return Response(user_data)


class CustomTokenRefreshView(APIView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = TokenRefreshSerializer(data=request.data)

        if serializer.is_valid():
            refresh_token = serializer.validated_data["refresh"]

            try:
                token = RefreshToken(refresh_token)
                return Response({"access": str(token.access_token)}, status=status.HTTP_200_OK)
            except Exception:
                return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)