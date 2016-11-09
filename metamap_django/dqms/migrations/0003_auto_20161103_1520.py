# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dqms', '0002_auto_20161103_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dqmsrule',
            name='measure_src',
        ),
        migrations.RemoveField(
            model_name='dqmsrule',
            name='rule_desc',
        ),
        migrations.AddField(
            model_name='dqmsrule',
            name='max',
            field=models.FloatField(default=-999),
        ),
        migrations.AddField(
            model_name='dqmsrule',
            name='measure_column',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u6570\u636e\u5217'),
        ),
        migrations.AddField(
            model_name='dqmsrule',
            name='measure_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u6307\u6807\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='dqmsrule',
            name='measure_type',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u6570\u636e\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='dqmsrule',
            name='min',
            field=models.FloatField(default=-999),
        ),
        migrations.AlterField(
            model_name='dqmscase',
            name='remark',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='dqmscase',
            name='sql_pattern',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='\u62bd\u53d6\u6570\u636e\u7684ETL'),
        ),
        migrations.AlterField(
            model_name='dqmsrule',
            name='rule_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u89c4\u5219\u7c7b\u578b'),
        ),
    ]