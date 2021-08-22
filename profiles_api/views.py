from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    serailizer_class = serializers.HelloSerializer

    """Testing APIView features"""
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function',
            'is similar to a django view'
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        serializer = self.serailizer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)