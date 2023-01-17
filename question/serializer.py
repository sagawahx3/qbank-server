from rest_framework import serializers
from question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'institute', 'version', 'question_number', 'body', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5', 'correct')