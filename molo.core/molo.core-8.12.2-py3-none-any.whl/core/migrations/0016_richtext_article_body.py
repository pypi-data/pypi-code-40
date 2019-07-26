# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-21 10:59
from __future__ import unicode_literals

from django.db import migrations
import django_enumfield.db.fields
import molo.core.blocks
import molo.core.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_freebasics_banner_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', molo.core.blocks.MarkDownBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('numbered_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Item'))), ('page', wagtail.core.blocks.PageChooserBlock()), ('media', molo.core.models.MoloMediaBlock(icon='media')), ('richtext', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        )
    ]
