from rest_framework import serializers
from userinfo.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user', 'totalAnswers', 'rightAnswers', 'wrongAnswers')