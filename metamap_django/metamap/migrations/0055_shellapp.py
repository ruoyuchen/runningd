# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-04-17 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('will_common', '0003_auto_20170510_0822'),
        ('metamap', '0054_auto_20171113_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShellApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'no_name_yet', max_length=100, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('rel_name', models.CharField(default=b'no_name_yet', max_length=100, verbose_name='\u53ef\u8bfb\u7684\u540d\u5b57')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.IntegerField(blank=True, default=5)),
                ('valid', models.IntegerField(choices=[(1, b'\xe6\x98\xaf'), (0, b'\xe5\x90\xa6')], default=1, verbose_name='\u662f\u5426\u751f\u6548')),
                ('content', models.TextField(blank=True, default=b'', null=True, verbose_name='shell\u5185\u5bb9')),
                ('cgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.OrgGroup')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.UserProfile')),
                ('exec_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='metamap.ExecObj')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]