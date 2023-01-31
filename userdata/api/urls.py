from django.urls import path, include, re_path
from .views import userDataFunc
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

router = DefaultRouter()
router.register('info', UserDataViewSet, basename='userdata')

urlpatterns = [
    re_path('first', userDataFunc),
    re_path('', include(router.urls))
]

