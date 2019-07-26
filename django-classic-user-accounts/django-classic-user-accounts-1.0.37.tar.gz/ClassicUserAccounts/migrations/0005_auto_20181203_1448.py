# Generated by Django 2.1.1 on 2018-12-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassicUserAccounts', '0004_user_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='theme',
            field=models.CharField(choices=[('default Theme', 'Default Theme'), ('theme-1', 'Theme-1'), ('theme-2', 'Theme-2'), ('theme-3', 'Theme-3')], default='default-theme', max_length=30),
        ),
    ]
