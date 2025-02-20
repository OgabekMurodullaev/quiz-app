from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password"]

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Bu username allqachon mavjud.")
        return username

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Parol 8 ta belgidan kam bo'lmasligi kerak!")
        return value

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"],
                                   first_name=validated_data["first_name"],
                                   last_name=validated_data["last_name"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Username yoki parol noto'g'ri")
        return {"user": user}


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
