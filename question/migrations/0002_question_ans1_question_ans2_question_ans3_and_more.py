# Generated by Django 4.1.5 on 2023-01-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ans1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ans2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ans3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ans4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ans5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='institute',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='version',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
