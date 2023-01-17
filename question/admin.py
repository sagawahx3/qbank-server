from django.contrib import admin
from question.models import Question


class Questions(admin.ModelAdmin):
    list_display = ('id', 'question_number', 'body', 'ans1', 'ans2', 'ans3', 'ans4', 'ans5')
    list_display_links = ('id', 'question_number')
    search_fields = ('id', 'question_number', 'body')


admin.site.register(Question, Questions)