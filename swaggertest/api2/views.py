from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SecondHelloView(APIView):
    def get(self, request):
        data = {
            'content': 'This is the response for api2'
        }
        return Response(data)