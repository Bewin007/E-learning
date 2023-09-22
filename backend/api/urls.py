from django.contrib import admin
from django.urls import path
from .views import * 

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('user', User_Create.as_view(), name='create-view-user'),
    path('bank', Bank_Detail_api.as_view(), name='register'),
    path('user/<int:user_id>/', User_Create.as_view(), name='edit-delete-user'),
    path('expert/<int:user_id>/', Expert_api.as_view(), name='delete-expert'),
    path('expert', Expert_api.as_view(), name='create-view-expert'),
    path('catogery', Catogery_api.as_view(), name='create-view-catogery'),
    path('gig', Gig_api.as_view(), name='create-view-gig'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)