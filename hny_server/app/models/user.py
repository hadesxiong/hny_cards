# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义用户主表
class UserMain(Model):

    usr_id = fields.CharField(max_length=64,unique=True)
    usr_type = fields.IntField(default=1)
    usr_class = fields.IntField(default=1)
    usr_create_dt = fields.DatetimeField(autonow=True,null=True)
    usr_update_dt = fields.DatetimeField(autonow=True,null=True)
    usr_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_user_main'

# 定义用户信息表
class UserInfo(Model):

    usr_id = fields.CharField(max_length=64,unique=True)
    usr_nick = fields.CharField(max_length=128)
    usr_avatar = fields.CharField(max_length=512,null=True)
    guest_id = fields.CharField(max_length=64,unique=True)
    info_create_dt = fields.DatetimeField(autonow=True,null=True)
    info_update_dt = fields.DatetimeField(autonow=True,null=True)
    info_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_user_info'

# 定义游客信息表
class GuestMain(Model):

    guest_id = fields.CharField(max_length=64,unique=True)
    guest_finger = fields.CharField(max_length=128,unique=True)
    guest_create_dt = fields.DatetimeField(autonow=True,null=True)
    guest_ext = fields.JSONField(null=True)

    class Meta:
        table = 'hny_guest_main'
