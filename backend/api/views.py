from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response

class Hello(APIView):
    def get(self, request):
        return Response("Hello")

