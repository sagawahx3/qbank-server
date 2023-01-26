from django.contrib.auth.models import User
from rest_framework import viewsets
from userinfo.models import UserInfo
from userinfo.serializer import UserInfoSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class UserInfoViewSet(viewsets.ModelViewSet):

    def get_object(self, pk):
        queryset = User.objects.get(id=pk)
        userinfo = UserInfo.objects.get(user=queryset)

        return get_object_or_404(UserInfo, username=queryset)

