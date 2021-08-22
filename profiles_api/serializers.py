from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.userInfo
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                
            }
        }