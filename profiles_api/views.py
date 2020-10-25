from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView greetings"""
        an_apiview = [
            'Hey!',
            'Hallo!',
            'Hola!',
        ]

        return Response({'message':'Hi there!', 'Greetings': an_apiview})