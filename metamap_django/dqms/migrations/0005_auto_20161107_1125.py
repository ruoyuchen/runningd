# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqms', '0004_auto_20161104_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='dqmscheck',
            name='cases',
            field=models.ManyToManyField(to='dqms.DqmsCase'),
        ),
        migrations.AddField(
            model_name='dqmscheck',
            name='schedule',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
