# Generated by Django 2.0.3 on 2018-03-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0023_client_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='reuse_consent',
            field=models.BooleanField(default=True, help_text="If enabled, server will save the user consent given to a specific client, so that user won't be prompted for the same authorization multiple times.", verbose_name='Reuse Consent?'),
        ),
    ]
