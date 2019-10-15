from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

class FarmUser(AbstractUser):
    user_name = models.CharField(max_length=30, null=True, blank=False)
    password = models.CharField(max_length=512, null=True, blank=False)
    name = models.CharField(max_length=30, null=True, blank=False)
    email = models.CharField(max_length=3, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=False, editable=False, null=True, blank=False)

class Roles(models.Model):
    name = models.CharField(max_length=60, null=True, blank=False)
    description = models.TextField(max_length=30, null=True, blank=False)
    ROLE_CHOICES = (
      (1, 'farmer'),
      (2, 'field_worker'),
      (3, 'ASO'),
      (4, 'credit officer'),
  )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)


class Permissions(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField()




class UserRoles(models.Model):
    role = models.ForeignKey(Roles, on_delete = models.CASCADE)

class PermissionsRoles(models.Model):
    permission = models.ForeignKey(Permissions, on_delete = models.CASCADE)
    role = models.ForeignKey(Roles, on_delete = models.CASCADE)

