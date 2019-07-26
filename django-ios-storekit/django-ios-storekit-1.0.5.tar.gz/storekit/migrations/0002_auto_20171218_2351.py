# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storekit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inapp',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='response',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
