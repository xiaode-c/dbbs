# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_img',
            field=models.ImageField(default='aaaa.png', upload_to=b'user_img'),
            preserve_default=False,
        ),
    ]