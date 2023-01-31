from django.urls import path, include, re_path
from .views import userDataFunc

urlpatterns = [
    re_path('first', userDataFunc)
]