from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    #Validates the input as well
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """"Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                #This is for the web
                'style': {'input_type': 'password'}
            }
        }

    #Overrides the create function to create new user in the db
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    #Overrides the default update function of the ModelSerializer
    #In the case of an update we pop the password from validated_data
    #and assing it to instanct to save it as a has
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            #Saves the password as a hash
            instance.set_password(password)
 
        return super().update(instance, validated_data)
