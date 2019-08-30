from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usermodels')
    def __str(self):
        return 'Profile for user {}'.format(self.user.username)
