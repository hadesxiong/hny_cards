# coding=utf8
from fastapi import APIRouter, Depends

from app.api.schema.sch_main import *
from app.api.controller.ctrl_main import *
from app.utils.security import get_current_user

# 定义路由
main_rt = APIRouter(prefix='/main', tags=['main'])

# 定义抽签接口
@main_rt.post('/qianCreate',
              response_model=QianRes,
              response_model_exclude_unset=True)

async def createQian(form_data:QianCreate,
                     current_user: str = Depends(get_current_user)):

    # 清理参数
    fltr_data = {k:v for k,v in form_data.model_dump().items() if v is not None}
    rslt = await create_qian_handler(
        qian_number = fltr_data.get('qian_number',None),
        usr_id = current_user
    )

    return QianRes(code=200, msg='success', target=rslt['id'], dt=rslt['dt'])

# 定义提交动作接口
@main_rt.post('/qianAction',
              response_model=QianRes,
              response_model_exclude_unset=True)

async def actionQian(form_data:QianAction,
                     current_user: str = Depends(get_current_user)):
    
    # 清理参数
    fltr_data = {k:v for k,v in form_data.model_dump().items() if v is not None}
    rslt = await action_qian_handler(
        action_target = fltr_data.get('action_target',None),
        usr_id = current_user,
        action_type = fltr_data.get('action_type', None)
    )

    return QianRes(code=200, msg='success', target=rslt['id'], dt=rslt['dt'])