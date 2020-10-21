from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    #Validates the input as well
    name = serializers.CharField(max_length=10)