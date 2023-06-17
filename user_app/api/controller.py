from django.db import IntegrityError
from rest_framework import serializers
from user_app.api.repository import UserRepository
from user_app.models import User
from user_app.utils import raw_upload_file_to_base64, base64_to_image_file


class UserController:

	@staticmethod
	def create_user(attrs):
		profile_string = raw_upload_file_to_base64(attrs["profile_picture"])
		# raw_data = base64_to_image_file(profile_string)
		# print(raw_data)
		attrs["profile_picture"] = profile_string

		try:
			response = UserRepository.create_user(attrs=attrs)
		except IntegrityError:
			raise serializers.ValidationError({"error": "User already exists"})

		return response

	@staticmethod
	def update_user(attrs):
		if "profile_picture" in attrs.keys():
			profile_string = raw_upload_file_to_base64(attrs["profile_picture"])
			attrs["profile_picture"] = profile_string

		try:
			user = UserRepository.get_user(email=attrs["email"])
		except User.DoesNotExist:
			raise serializers.ValidationError({"error": "User does not exist"})

		UserRepository.update_user(attrs=attrs,user=user)

	@staticmethod
	def get_user(email):
		try:
			user = UserRepository.get_user(email=email)
		except User.DoesNotExist:
			raise serializers.ValidationError({"error": "User does not exist"})
		return user