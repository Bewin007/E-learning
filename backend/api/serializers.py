from rest_framework import serializers
from rest_framework import exceptions

from .models import *

class Bank_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Details
        fields = '__all__'

class Users_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    bank_details = Bank_Details_Serializer()
    class Meta:
        model = User
        fields = '__all__'

class User_Bank_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bank_details']

class ExpertSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    class Meta:
        model = Expert
        fields = '__all__'

class Expert_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Gig_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'

class GigSerializer(serializers.ModelSerializer):
    expert = ExpertSerializer()
    class Meta:
        model = Gig
        fields = '__all__'