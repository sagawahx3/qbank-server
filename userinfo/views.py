from rest_framework import viewsets
from userinfo.models import UserInfo
from userinfo.serializer import UserInfoSerializer


# Create your views here.
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.get_object_or_404(UserInfo, user=id)
    serializer_class = UserInfoSerializer
