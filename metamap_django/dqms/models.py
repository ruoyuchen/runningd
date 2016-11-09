# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class DqmsDatasource(models.Model):
    src_name = models.CharField(max_length=300, blank=True, null=True)
    src_type = models.CharField(max_length=300, blank=True, null=True)
    src_desc = models.CharField(max_length=300, blank=True, null=True)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)
    valid = models.IntegerField(default=1)

    class Meta:
        db_table = 'willdqms_datasource'


class DqmsCase(models.Model):
    case_name = models.CharField(max_length=300, blank=True, null=True)
    creator = models.CharField(max_length=300, blank=True, null=True)
    editor = models.CharField(max_length=300, blank=True, null=True)
    datasrc = models.ForeignKey(DqmsDatasource, on_delete=models.CASCADE, null=False)
    query = models.CharField(max_length=3000, blank=True, null=True)
    sql_pattern = models.CharField(max_length=3000, blank=True, null=True, verbose_name=u'抽取数据的ETL')
    column_name = models.CharField(max_length=3000, blank=True, null=True)
    data_dimension = models.CharField(max_length=3000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    param = models.CharField(max_length=300, blank=True, null=True)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'备注')

    class Meta:
        db_table = 'willdqms_case'


class DqmsCaseInst(models.Model):
    case = models.ForeignKey(DqmsCase, on_delete=models.CASCADE, null=False)
    result_code = models.IntegerField(blank=True, null=True)
    result_mes = models.CharField(max_length=1000, blank=True, null=True)
    is_schedule = models.IntegerField(blank=True, null=True)
    is_ack = models.IntegerField(blank=True, null=True)
    ack_count = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_case_inst'


class DqmsCheck(models.Model):
    chk_name = models.CharField(max_length=300, blank=True, null=True)
    creator = models.CharField(max_length=300, blank=True, null=True)
    editor = models.CharField(max_length=300, blank=True, null=True)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=300, blank=True, null=True)
    schedule = models.CharField(max_length=30, blank=True, null=True)
    cases = models.ManyToManyField(DqmsCase)
    valid = models.IntegerField(default=1)

    class Meta:
        db_table = 'willdqms_check'


class DqmsCheckCase(models.Model):
    chk = models.ForeignKey(DqmsCheck, on_delete=models.CASCADE, null=False)
    case = models.ForeignKey(DqmsCase, on_delete=models.CASCADE, null=False)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_check_case'
        unique_together = (('chk', 'case'),)


class DqmsCheckInst(models.Model):
    chk = models.ForeignKey(DqmsCheck, on_delete=models.CASCADE, null=False)
    case_num = models.IntegerField(blank=True, null=True)
    case_finish_num = models.IntegerField(blank=True, null=True)
    result_code = models.IntegerField(blank=True, null=True)
    result_mes = models.CharField(max_length=300, blank=True, null=True)
    is_schedule = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_check_inst'


class DqmsIndex(models.Model):
    case = models.ForeignKey(DqmsCase, on_delete=models.CASCADE, null=False)
    idx_name = models.CharField(max_length=300, blank=True, null=True)
    data_type = models.CharField(max_length=300, blank=True, null=True)
    col_name = models.CharField(max_length=300, blank=True, null=True)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'willdqms_index'


class DqmsIndexInst(models.Model):
    index = models.ForeignKey(DqmsIndex, on_delete=models.CASCADE, null=False)
    case = models.ForeignKey(DqmsCase, on_delete=models.CASCADE, null=False)
    chkinst = models.ForeignKey(DqmsCheckInst, on_delete=models.CASCADE, null=False)
    result_code = models.IntegerField(blank=True, null=True)
    result_mes = models.CharField(max_length=1000, blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_index_inst'


class DqmsRule(models.Model):
    case = models.ForeignKey(DqmsCase, on_delete=models.CASCADE, null=False)
    rule_type = models.IntegerField(blank=True, null=True,verbose_name=u'规则类型')
    max = models.IntegerField(default=-999)
    min = models.IntegerField(default=-999)
    measure_name = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'指标名称')
    measure_type = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'数据类型')
    measure_column = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'数据列')
    measure_desc = models.CharField(max_length=300, blank=True, null=True)
    measure_param = models.CharField(max_length=300, blank=True, null=True)
    rule_predicate = models.CharField(max_length=300, blank=True, null=True)

    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'willdqms_rule'


class DqmsRuleInst(models.Model):
    rule = models.ForeignKey(DqmsRule, on_delete=models.CASCADE, null=False)
    result_code = models.IntegerField(blank=True, null=True)
    result_mes = models.CharField(max_length=1000, blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_rule_inst'


class DqmsView(models.Model):
    viewer = models.CharField(max_length=300, blank=True, null=True)
    chk = models.ForeignKey(DqmsCheck, on_delete=models.CASCADE, null=False)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_view'


class DqmsAck(models.Model):
    caseins = models.ForeignKey(DqmsCaseInst, on_delete=models.CASCADE, null=False)
    result_msg = models.CharField(max_length=5000, blank=True, null=True)
    ack_user = models.CharField(max_length=300, blank=True, null=True)
    ctime = models.DateTimeField(default=timezone.now)
    utime = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'willdqms_ack'