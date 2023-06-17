from rest_framework import serializers
from rest_framework import request
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from user_app.api.controller import UserController
from user_app.models import User


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "profile_picture", "bio"]


class CreateUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile_picture = serializers.ImageField()
    bio = serializers.CharField(required=False)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )  # for not showing password at input

    def validate(self, attrs):
        response = UserController.create_user(attrs=attrs)
        return response


class UpdateUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False)
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )  # for not showing password at input

    def validate(self, attrs):
        try:
            user = User(
                username=attrs["username"],
                email=attrs["email"],
                first_name=attrs["first_name"],
                last_name=attrs["last_name"],
            )
        except IntegrityError:
            raise serializers.ValidationError({"error": "User already Exists"})

        password = attrs["password"]
        user.set_password(password)
        user.save()

        # creating token manually using JWT and returning once user successfully registers
        refresh = RefreshToken.for_user(user)

        return {
            "user": UserResponseSerializer(user).data,
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        }


class GetUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class GetUserSerializer(serializers.Serializer):
    def validate(self, attrs):
        email = self.context["email"]
        user = UserController.get_user(email=email)
        serialized_data = UserResponseSerializer(user).data
        return serialized_data


class LoginViewSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(
        max_length=50, write_only=True, style={"input_type": "password"}
    )

    def validate(self, attrs):
        try:
            user = User.objects.get(username=attrs["username"])
        except Exception as e:
            user = None
        if user is not None:
            if user.check_password(attrs["password"]):
                refresh = RefreshToken.for_user(user)
                return {
                    "token": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                }
            else:
                raise serializers.ValidationError({"error": "Invalid Password"})
        else:
            raise serializers.ValidationError({"error": "User doesn't exists"})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"