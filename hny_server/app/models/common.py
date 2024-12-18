# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义字典表
class DictMain(Model):

    dict_id = fields.CharField(max_length=64, unique=True)
    dict_index = fields.CharField(max_length=128)
    dict_code = fields.IntField(default=1)
    dict_value = fields.CharField(max_length=128)
    dict_name = fields.CharField(max_length=128)
    dict_statu = fields.IntField(default=1)
    dict_create_dt = fields.DatetimeField(null=True, auto_now=True)
    dict_update_dt = fields.DatetimeField(null=True, auto_now=True)
    dict_create_usr = fields.CharField(max_length=64)
    dict_update_usr = fields.CharField(max_length=64)
    dict_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_dict_main'
        unique_together = ('dict_index','dict_code','dict_name')