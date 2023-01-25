from rest_framework import serializers
from userinfo.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'institute', 'version', 'question_number', 'body', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'correct')