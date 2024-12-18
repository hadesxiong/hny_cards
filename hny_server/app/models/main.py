# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义签表
class QianMain(Model):

    qian_id = fields.CharField(max_length=64,unique=True)
    qian_number = fields.IntField(default=1)
    qian_tiangan = fields.CharField(max_length=32)
    qian_type = fields.CharField(max_length=32)
    qian_sentence = fields.CharField(max_length=128)
    qian_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_qian_main'

# 定义签记录
class QianRecord(Model):

    record_id = fields.CharField(max_length=64,unique=True)
    qian_number = fields.IntField(default=0)
    record_create_by= fields.CharField(max_length=64)
    record_create_dt = fields.DatetimeField(autonow=True,null=True)
    record_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_qian_record'

# 定义动作表
class ActionMain(Model):

    action_id = fields.CharField(max_length=64,unique=True)
    action_type = fields.IntField(default=1)
    action_target = fields.CharField(max_length=128,default='homepage')
    action_by = fields.CharField(max_length=128)
    action_create_dt = fields.DatetimeField(autonow=True,null=True)
    action_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_action_main'