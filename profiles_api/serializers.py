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
        model = models.profilePrefrence
        fields = ('id','user_info','preference','modified_on')
        extra_kwargs={'user_info':{'read_only':True}}

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.articles
        fields = '__all__'
        extra_kwargs={'user_info':{'read_only':True}, 'title':{'read_only':True}, 'description':{'read_only':True}, 'IMAGE':{'read_only':True}}


