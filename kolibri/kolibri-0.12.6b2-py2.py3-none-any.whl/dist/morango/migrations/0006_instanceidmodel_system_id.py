# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-30 00:15
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("morango", "0005_auto_20170629_2139")]

    operations = [
        migrations.AddField(
            model_name="instanceidmodel",
            name="system_id",
            field=models.CharField(blank=True, max_length=100),
        )
    ]
