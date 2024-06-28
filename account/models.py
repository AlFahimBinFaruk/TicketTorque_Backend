from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from django.contrib.auth.hashers import make_password,check_password


import uuid


class Account(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)






    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


    def __str__(self):
        return self.email

    def set_password(self,password):
        self.password=make_password(password)

    def check_password(self,password):
        return check_password(password,self.password)

    class Meta:
        db_table = 'account'
