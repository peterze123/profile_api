from rest_framework import serializers
from newsapi import NewsApiClient

from profiles_api import models
from .models import articles

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.userInfo
        fields = ('id', 'email', 'name', 'password','preference')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }
    
    def create(self, validated_data):
        """create and return a new user"""
        user = models.userInfo.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """updating user info"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileCategorySerializer(serializers.ModelSerializer):
    """serializes the category for profile"""
    """could used for adding comment functions"""
    class Meta:
        model = models.profileFeed
        fields = ('id','user_info','text','modified_on','article_info')
        extra_kwargs={'user_info':{'read_only':True}, 'article_info':{'required':False}}


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.articles
        fields = '__all__'
        extra_kwargs = {'IMAGE': {"required": False, "allow_null": True}}
