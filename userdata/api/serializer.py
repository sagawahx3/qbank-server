from rest_framework import serializers
from userdata.models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['user', 'answeredQuestions', 'wrongQuestions', 'rightQuestions']