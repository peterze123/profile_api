from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class userInfoManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email is a required field')

        email = self.normalize_email(email)
        user = self.model(email = email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,name, password):
        user = self.create_user(email, name, password)

        user.is_staff=True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class userInfo(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = userInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.email

class profilePrefrence(models.Model):
    """Profile's prefrence of news"""  
    user_info = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    
    categories = [('business','business'),
    ('entertainment','entertainment'),
    ('general','general'),
    ('health','health'),
    ('science','science'),
    ('sports','sports'),
    ('technology','technology'),]
    
    preference = models.CharField(max_length=13, choices=categories, default='general')
    changed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preference