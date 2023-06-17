from user_app.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserRepository:

	@staticmethod
	def create_user(attrs):
		password = attrs["password"]
		attrs.pop("password", None)
		user = User(**attrs)

		user.set_password(password)
		user.save()

		# creating token manually using JWT and returning once user successfully registers
		refresh = RefreshToken.for_user(user)

		return {
			"token": {
				"refresh": str(refresh),
				"access": str(refresh.access_token)
			}
		}

	@staticmethod
	def update_user(user, attrs):
		if "password" in attrs.keys():
			user.set_password(attrs["password"])

		for attribute, value in attrs.items():
			user.__setattr__(attribute, value)

		user.save()

	@staticmethod
	def get_user(email):
		return User.objects.get(email=email)