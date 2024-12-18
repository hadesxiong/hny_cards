# coding=utf8

from fastapi import APIRouter, Depends, Query

from app.api.schema.sch_base import *
from app.api.controller.ctrl_base import *
from app.core.config import settings

# 定义路由
base_rt = APIRouter(prefix='/base', tags=['base'])

# 定义游客登陆接口
@base_rt.post('/guestLogin',
              response_model=GuestLoginResponse,
              response_model_exclude_unset=True)

async def loginGuest(form_data:GuestLoginRequest):

    # 清理参数
    fltr_data = {k:v for k,v in form_data.model_dump().items() if v is not None}
    token_data = await login_guest_handler(fltr_data.get('finger'))
    return GuestLoginResponse(code=200, msg='success', token=token_data)