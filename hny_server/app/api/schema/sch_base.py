# coding=utf8

from pydantic import BaseModel, Field

from app.api.schema.basic import ResBasic

# 定义一个访客登陆的请求
class GuestLoginRequest(BaseModel):

    finger: str | None = Field(default=None, alias='signature')

    class Config:
        
        extra = 'forbid'

# 定义一个基本回复的请求
class GuestLoginResponse(ResBasic):

    token: str | None = Field(default=None)