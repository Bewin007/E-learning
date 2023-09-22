from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from .serializers import *
class Hello(APIView):
    def get(self, request):
        return Response("Hello")

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class User_Create(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_users = [UsersSerializer(user).data for user in users]
        return Response(serialized_users)
    
    def post(self, request):
        serializer = Users_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = User_Bank_Update_Serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        

class Bank_Detail_api(APIView):
    def get(self,request):
        data = Bank_Details.objects.all()
        serializer = Bank_Details_Serializer(data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Bank_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ExpertListView(generics.ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

class Expert_api(APIView):
    def get(self, request):
        users = Expert.objects.all()
        serialized_users = [ExpertSerializer(user).data for user in users]
        return Response(serialized_users)
    
    def post(self, request):
        serializer = Expert_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, user_id):
        try:
            user = Expert.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)