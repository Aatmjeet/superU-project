from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        email,
        password,
        **extra_fields,
    ):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        first_name,
        last_name,
        email,
        password,
        **extra_fields,
    ):
        return self.create_user(
            first_name,
            last_name,
            email,
            password,
            **extra_fields,
        )
