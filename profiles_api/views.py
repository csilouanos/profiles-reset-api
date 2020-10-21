from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

#You define a url and is assigned to this view
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    # Retrieves a list of objects or an object
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to the traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        #Django expects to return a response
        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # Standard way to return data from request
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})