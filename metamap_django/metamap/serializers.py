# !/usr/bin/env python
# -*- coding: utf-8 -*
'''
created by will 
'''
from rest_framework import serializers

from metamap.models import ETL, AnaETL, Exports, WillDependencyTask, BIUser


class ETLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ETL
        fields = ('tblName', 'valid', 'id')

class BIUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BIUser
        fields = ('username',)

class AnaETLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnaETL
        fields = ('name', 'valid', 'id')

class WillTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WillDependencyTask
        fields = ('name', 'valid', 'id')


class ExportsSerializer(serializers.HyperlinkedModelSerializer):
    task = WillTaskSerializer(required=True)
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Exports
        fields = ('file_loc', 'start_time', 'end_time', 'command', 'task')