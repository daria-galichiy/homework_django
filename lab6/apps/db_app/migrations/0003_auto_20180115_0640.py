# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0002_auto_20180114_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_photo',
            field=models.ImageField(blank=True, default='static/imgs/def.jpg', null=True, upload_to='static/imgs/'),
        ),
    ]
