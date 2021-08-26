from django.db.models import query
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from .models import articles
from newsapi import NewsApiClient


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    """Testing APIView features"""
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function',
            'is similar to a django view'
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        return Response({'message': 'Hello'})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response ({'message': message})
        else:
            return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.userInfo.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name','email', )

class UserLoginApiView(ObtainAuthToken):
    """login token authentication for the profiles"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserCategoryViewSet(viewsets.ModelViewSet):
    """Handles the category variable for each profile"""
    authentication_classes= (TokenAuthentication, )
    serializer_class = serializers.ProfileCategorySerializer
    queryset = models.profilePrefrence.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """set the profile of logged in user"""
        serializer.save(user_info=self.request.user)

    def create(self, request):
        """updates the articles after a profile's preference is set"""
        newsapi = NewsApiClient(api_key = '2fe5b1793acc49adb3e4484c9ead5d87')
        top = newsapi.get_top_headlines(sources='teachcrunch')
        #
        news = top['articles']
        for i in range(len(news)):
            f = news[i]
            articles.user_info = self.request.user
            articles.title = f['title']
            articles.description = f['description']
            articles.IMAGE = f['urlToImage']
            articles.save()
        return Response({'message': 'Articles Updated'})
    
    def update(self, request):
        self.create()