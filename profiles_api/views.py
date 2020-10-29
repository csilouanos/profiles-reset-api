from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.decorators import action

#ObtainAuthToken is a Django view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
        
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an oject"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an oject"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

#We connect the serializer class
#By just setting the serializer_class and the queryset ModelViewSet
#has already implemented all the required methods update, create etc
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) #, is to create a tuple instead of single item
    permission_classes = (permissions.UpdateOwnProfile,)
    #Add filter backend for search filter
    filter_backends = (filters.SearchFilter,)
    #Django will allow us search only by name and email fields
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    #Enables the django UI (?)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    #Users can only update statuses when user is authenticated
    #IsAuthenticated ensures that the current ViewSet is not visible (feed endpoint)
    #by the user unless is logged in
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    # likes = models.ProfileFeedItemLike.objects.all()

    #Called in every Http POST (create is called)
    #Save the relation ship item (user_profile)
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

    # @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    # def likes(self, request, pk=None):
    #     """Gets the likes"""
    #     feed_item = self.get_object()
    #     print("UserProfileFeedViewSet: get likes feed item ", feed_item.id)
    #     likes = feed_item.likes.all()
    #     serializer = serializers.ProfileFeedItemLikeSerializer(likes)
    #     return Response(serializer.data)

    # @action(methods=['post'], detail=False, permission_classes=[IsAuthenticated])
    # def likes(self, request):
    #     """Creates a like"""
    #     feed_item = self.get_object()
    #     print("UserProfileFeedViewSet: post like feed item ", feed_item.id)



class UserProfileFeedLikeViewSet(viewsets.ModelViewSet):
    """Handles creating and deleting like item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemLikeSerializer
    queryset = models.ProfileFeedItemLike.objects.all()
    permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     """Sets the user profile to the model"""
    #     serializer.save(user_profile=self.request.user)
    #     # serializer.save()
        
