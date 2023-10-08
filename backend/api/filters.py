import django_filters
from .models import *

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
    email = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type'] 

class ExpertFilter(django_filters.FilterSet):
    display_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
    expert_experience = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
    class Meta:
        model = Expert
        fields = ['display_name', 'expert_experience']  # Add more fields as needed

# class GigFilter(django_filters.FilterSet):
#     display_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
#     expert_experience = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
#     class Meta:
#         model = Gig
#         fields = ['display_name', 'expert_experience']  # Add more fields as needed
