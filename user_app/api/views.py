from django.http import HttpResponse, HttpRequest
from rest_framework import response
from rest_framework.generics import GenericAPIView
from .serializer import (
    CreateUserSerializer,
    GetUserSerializer,
    UpdateUserSerializer,
    LoginViewSerializer,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class UserView(GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_permission_class(self):
        if self.request.method == 'POST':
            return AllowAny
        elif self.request.method == 'PATCH':
            return IsAuthenticated
        # For any other request methods, deny permission by default
        return None

    def get_serializer_class(self):
        if self.request.method == "POST":
            serializer_class = CreateUserSerializer
        elif self.request.method == "PATCH":
            serializer_class = UpdateUserSerializer

        return serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            {
                "message": "User created successfully!",
                **serializer.validated_data,
            }
        )

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            {
                "message": "User updated successfully!",
                **serializer.validated_data,
            },
            status=status.HTTP_201_CREATED
        )


class GetUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetUserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.kwargs)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            serializer.validated_data,
            status=status.HTTP_200_OK,
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {"email": self.kwargs["email"]},
        )
        return context


class LoginUserView(GenericAPIView):
    serializer_class = LoginViewSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {
                "msg": "Login successful",
                **serializer.validated_data,
            },
            status=status.HTTP_202_ACCEPTED
        )


class LogoutView(GenericAPIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return response.Response({"msg": "Logout Successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                {"msg": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST
            )
