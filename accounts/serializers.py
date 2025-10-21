from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    email = serializers.EmailField(validators=[EmailValidator()], max_length=254)
    password = serializers.CharField(write_only=True, min_length=8)
    password_check = serializers.CharField(write_only=True, min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already used.")
        return value

    def validate(self, data):
        if data.get("password") != data.get("password_check"):
            raise serializers.ValidationError({"password_check": "Passwords do not match."})
        try:
            validate_password(data.get("password"))
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return data

    def create(self, validated_data):
        validated_data.pop("password_check", None)
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user
