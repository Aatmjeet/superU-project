from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from user_app.manager import UserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
# Custom user model
class User(AbstractUser, PermissionsMixin):
    objects = UserManager()

    id = models.AutoField(_("Unique identifier for user"),primary_key=True,editable=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    profile_picture = models.CharField(max_length=100000, blank=False, null=False)

    EMAIL_FIELD = "email"

    class Meta:
        db_table = "tbl__user"

# now we are writing extra fields, so we need to write model manager file(manager.py)
