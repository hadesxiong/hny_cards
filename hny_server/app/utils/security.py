# coding=utf8

import jwt

from bson.objectid import ObjectId
from datetime import datetime, timezone, timedelta
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from typing import Annotated

from app.core.config import settings
from app.models.user import *
from app.core.error import CustomHTTPException

# 注册游客用户
async def register_guest(guest_model: GuestMain, finger:str):

    # 查找指纹
    try:
        guest_rslt = await GuestMain.filter(guest_finger=finger)
        return guest_rslt[0].guest_id
    except:
        guest_data = {}
        guest_data.update({
            'guest_id': f'guest_{ObjectId()}',
            'guest_finger': finger,
            'guest_create_dt': datetime.now(timezone(timedelta(hours=8)))
        })

        guest_rslt = await guest_model.create(**guest_data)
        return guest_rslt.guest_id

# 注册用户信息
async def register_user(guest_id:str):

    # 查找游客信息
    try:
        guest_rslt = await GuestMain.filter(guest_id=guest_id)
        user_info = {}
        user_info.update ({
            'usr_id': f'usr_{ObjectId()}',
            'usr_nick': f'user_{ObjectId()[0:9]}',
            'guest_id': guest_rslt[0].guest_id,
            'info_create_dt': datetime.now(timezone(timedelta(hours=8)))
        })
        info_rslt = await UserInfo.create(**user_info)

        user_main = {}
        user_main.update({
            'usr_id': info_rslt.usr_id,
            'usr_type': 1,
            'usr_class': 2,
            'usr_create_dt': info_rslt.usr_create_dt
        })
        main_rslt = await UserMain.create(**user_main)

        return main_rslt.usr_id
    
    except:
        return guest_id

# 查询游客用户
async def get_guest(guest_model:GuestMain, finger:str):

    guest_ins = await guest_model.filter(guest_finger=finger)

    if len(guest_ins) == 0:
        guest_id = await register_guest(guest_model, finger)
        return guest_id
    
    else:
        return guest_ins[0].guest_id
    
# 创建token
def create_token(data:dict, expires_delta: timedelta | None = None):

    to_encode = data.copy()
    # print(data)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(hours=2)

    to_encode.update({'exp': expire})

    encode_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm = settings.ALGORITHM
    )

    return encode_jwt

# 获取当前游客
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_guest(token: Annotated[str, Depends(oauth2_scheme)]):

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms= [settings.ALGORITHM]
        )
        print(payload)
        guest_id: str = payload.get('guest')

        if not guest_id:
            raise CustomHTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = '用户验证失败',
                err_code = 11002
            )
        
        try:
            guest_ins = await GuestMain.get(guest_id=guest_id)
            return guest_ins.guest_id
        
        except:
            raise CustomHTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = '用户验证失败',
                err_code = 11003
            )
        
    except ExpiredSignatureError:
        raise CustomHTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = 'token已过期',
            err_code = '11007'
        )
    
    except InvalidTokenError:
        raise CustomHTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = '用户验证失败',
            err_code = '11004'
        )