from django.contrib import admin
from django.urls import path,include
from .views import * 
from .viewset import UserViewSet, ExpertViewSet

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

#filter
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'experts', ExpertViewSet)



urlpatterns = [
    path('user', User_Create.as_view(), name='create-view-user'),
    path('user/<int:user_id>/', User_Create.as_view(), name='edit-delete-user'),
    path('bank', Bank_Detail_api.as_view(), name='register'),
    path('expert/<int:user_id>/', Expert_api.as_view(), name='delete-expert'),
    path('expert', Expert_api.as_view(), name='create-view-expert'),
    path('catogery', Catogery_api.as_view(), name='create-view-catogery'),
    path('gig', Gig_api.as_view(), name='create-view-gig'),
    path('review', Review_api.as_view(), name='create-view-review'),
    path('faq', FAQ_api.as_view(), name='create-view-review'),
    path('replay', Replay_api.as_view(), name='create-view-review'),
    path('gig-package', Gig_package_api.as_view(), name='create-view-review'),
    path('order', Order_api.as_view(), name='create-view-review'),
    path('expert-category', Expert_Catogery_api.as_view(), name='create-view-review'),
    path('wishlist', Wishlist_api.as_view(), name='create-view-review'),
    path('call', Call_Details_api.as_view(), name='create-view-review'),
    path('notification', Notification_api.as_view(), name='create-view-review'),
    path('id/<int:pk>', User_id_search.as_view(), name='id-search'),
    path('email/<str:pk>', User_email_search.as_view(), name='id-email'),
    path('user-pag/', User_paging.as_view()),

    path('api/', include(router.urls)),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)