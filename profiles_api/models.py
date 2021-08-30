from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models.deletion import CASCADE

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

categories = [('business','business'),
    ('entertainment','entertainment'),
    ('general','general'),
    ('health','health'),
    ('science','science'),
    ('sports','sports'),
    ('technology','technology'),]

class userInfo(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    preference = models.CharField(max_length=13, choices= categories, default='general')

    objects = userInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email

class profileFeed(models.Model):
    """Profile's comments toward an article or feed of any type"""  
    user_info = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    article_info = models.ForeignKey(
        'articles',
        on_delete = models.CASCADE
    )
    text = models.TextField()
    modified_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class articles(models.Model):
    """model that stores information, in this case I'm assuming this api is used for a news website"""

    preference = models.CharField(max_length=13, choices= categories, default='general')
    title = models.CharField(max_length=255)
    description = models.TextField()
    IMAGE = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title + ' (' + self.preference + ')'
