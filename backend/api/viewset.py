from rest_framework import viewsets, filters
from .models import User, Expert
from .filters import UserFilter, ExpertFilter
from .serializers import UsersSerializer, ExpertSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  # Use DjangoFilterBackend here
    filterset_class = UserFilter
    search_fields = ['username', 'email'] 

class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  # Use DjangoFilterBackend here
    filterset_class = ExpertFilter
    search_fields = ['display_name', 'expert_experience']

