# Generated by Django 4.1.5 on 2023-01-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_question_ans1_question_ans2_question_ans3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.PositiveIntegerField(max_length=1, null=True),
        ),
    ]
