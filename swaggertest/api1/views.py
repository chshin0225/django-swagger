from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloView(APIView):
    def get(self, request):
        data = {
            'content': 'Hello! api1 is successfully requested'
        }
        return Response(data)