# Generated by Django 2.1 on 2018-10-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
