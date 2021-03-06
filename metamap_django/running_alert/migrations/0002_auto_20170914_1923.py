# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-14 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('will_common', '0003_auto_20170510_0822'),
        ('running_alert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparkMonitorInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('utime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4')),
                ('instance_name', models.CharField(max_length=300, verbose_name='\u76d1\u63a7\u540d\u79f0')),
                ('exporter_uri', models.CharField(max_length=50, verbose_name='\u76d1\u63a7\u6307\u6807\u5730\u5740')),
                ('valid', models.IntegerField(choices=[(1, '\u662f'), (0, '\u5426')], default=1, verbose_name='\u662f\u5426\u6709\u6548')),
                ('cgroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.OrgGroup', verbose_name='\u6240\u5c5e\u7ec4\u7ec7')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.UserProfile', verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='cgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.OrgGroup', verbose_name='\u6240\u5c5e\u7ec4\u7ec7'),
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='will_common.UserProfile', verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='ctime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='host_and_port',
            field=models.CharField(max_length=50, verbose_name='\u76ee\u6807\u4e3b\u673a:\u7aef\u53e3\u53f7[10.2.16.81:4545]'),
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='service_type',
            field=models.CharField(choices=[('kafka', 'kafka'), ('zookeeper', 'zookeeper'), ('flume', 'flume')], max_length=50, verbose_name='\u5b9e\u4f8b\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='monitorinstance',
            name='utime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='servicerules',
            name='ctime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='servicerules',
            name='service_name',
            field=models.CharField(choices=[('kafka', 'kafka'), ('zookeeper', 'zookeeper'), ('flume', 'flume')], max_length=50, verbose_name='\u670d\u52a1\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='servicerules',
            name='utime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6700\u8fd1\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
