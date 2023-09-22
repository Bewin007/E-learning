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

class Review_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    expert = ExpertSerializer()
    client = UsersSerializer()
    gig = GigSerializer()
    class Meta:
        model = Review
        fields = '__all__'

class FAQ_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    gig = GigSerializer()
    class Meta:
        model = FAQ
        fields = '__all__'

class Replay_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Replay
        fields = '__all__'

class ReplaySerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    expert = ExpertSerializer()
    class Meta:
        model = Replay
        fields = '__all__'

class Gig_package_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gig_package
        fields = '__all__'

class Gig_packageSerializer(serializers.ModelSerializer):
    gig = GigSerializer()
    class Meta:
        model = Gig_package
        fields = '__all__'

class Order_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    gig = GigSerializer()
    client = UsersSerializer()
    expert = ExpertSerializer()
    gig_package = Gig_package()
    class Meta:
        model = Order
        fields = '__all__'

class Expert_Catogery_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expert_Catogery
        fields = '__all__'

class Expert_CatogerySerializer(serializers.ModelSerializer):
    expert = ExpertSerializer()
    category = CategorySerializer()
    class Meta:
        model = Expert_Catogery
        fields = '__all__'

class Wishlist_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    client = UsersSerializer()
    gig = GigSerializer()
    class Meta:
        model = Wishlist
        fields = '__all__'

class Call_Details_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Call_Details
        fields = '__all__'

class Call_DetailsSerializer(serializers.ModelSerializer):
    client = UsersSerializer()
    expert = ExpertSerializer()
    class Meta:
        model = Call_Details
        fields = '__all__'

class Notification_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    class Meta:
        model = Notification
        fields = '__all__'