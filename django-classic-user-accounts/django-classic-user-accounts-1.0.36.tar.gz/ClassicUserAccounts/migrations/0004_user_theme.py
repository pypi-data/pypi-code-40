# Generated by Django 2.1.1 on 2018-12-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassicUserAccounts', '0003_user_user_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='theme',
            field=models.CharField(choices=[('Default Theme', 'default-theme'), ('Theme-1', 'theme-1'), ('Theme-2', 'theme-2'), ('Theme-3', 'theme-3')], default='default-theme', max_length=30),
        ),
    ]
