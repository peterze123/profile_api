from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class userInfoManager(BaseUserManager):

    def create_usr(self, email, name, password=None):
        if not email:
            raise ValueError('Email is a required field')

        email = self.normalize_email(email)
        user = self.model(email = email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_admin(self, email, name, password):
        user = self.create_usr(email, name, password)

        user.is_superuser = True
        user.save(using=self._db)\

        return user

class userInfo(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    objects = userInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FOELDS = ['userId']

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.email

