from rest_framework.views import APIView
from rest_framework.response import Response


#You define a url and is assigned to this view
class HelloApiView(APIView):
    """Test API View"""
    
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