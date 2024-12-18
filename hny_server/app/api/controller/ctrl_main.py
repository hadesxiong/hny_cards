# coding=utf8

from bson.objectid import ObjectId
from datetime import datetime, timezone, timedelta
from typing import Dict, Any

from app.models.main import *
from app.models.common import *
from app.core.error import CustomHTTPException

# 提交生成灵签
async def create_qian_handler(
        qian_number: int | None = None,
        usr_id: str | None = None):
    
    if qian_number and usr_id:

        record_data = {}
        record_data.update({
            'record_id': f'record_{ObjectId()}',
            'qian_number': qian_number,
            'record_create_by': usr_id,
            'record_create_dt': datetime.now(timezone(timedelta(hours=8)))
        })

        record_rslt = await QianRecord.create(**record_data)

        return {
            'id': record_rslt.record_id[7:],
            'dt': datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
        }
    
    else:
        raise CustomHTTPException(status_code=400, detail='数据错误',err_code=40002)

# 提交动作数据
async def action_qian_handler(
        action_target: str | None = None,
        usr_id: str | None = None,
        action_type: str | None = None):
    
    if action_target and usr_id and action_type:

        dict_ins = await DictMain.filter(dict_index='action_type', dict_value=action_type).all()
        record_ins = await QianRecord.filter(record_id=action_target).all()

        if len(dict_ins) > 0 and len(record_ins) > 0:

            action_data = {}
            action_data.update({
                'action_id': f'action_{ObjectId()}',
                'action_type': dict_ins[0].dict_code,
                'action_target': action_target,
                'action_by': usr_id,
                'action_create_dt': datetime.now(timezone(timedelta(hours=8)))
            })

            action_rslt = await ActionMain.create(**action_data)

            return {
                'id': action_rslt.action_id[7:],
                'dt': datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
            }

        else:
            raise CustomHTTPException(status_code=400, detail='数据错误', err_code=40002)
    
    else:
        raise CustomHTTPException(status_code=400, detail='数据缺失', err_code=40014)