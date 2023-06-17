from django.urls import path, include
from .views import (
    UserView,
    GetUserView,
    LoginUserView,
    LogoutView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # auth related
    path("user/", UserView().as_view(), name="user views"),
    path("user/<str:email>/", GetUserView.as_view(), name="get user"),
    path("login/", LoginUserView().as_view(), name="login_view"),
    path("logout/", LogoutView().as_view(), name="logout_view"),
    # token related
    path("api/token/", TokenObtainPairView().as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView().as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
