# coding=utf8

from pydantic import BaseModel, Field
from typing import List, Dict, Any

from app.api.schema.basic import ResBasic

# 定义抽签行为
class QianCreate(BaseModel):

    qian_number: int | None = Field(default=1, alias='qian')
    
    class Config:
        extra = 'forbid'

# 定义提交行为
class QianAction(BaseModel):

    action_target: str | None = Field(default=None, alias='qian')
    action_type: str | None = Field(default=None, alias='type')
    
    class Config:
        extra = 'forbid'

# 定义提交结果
class QianRes(ResBasic):

    target: str | Dict[str,Any] | None = Field(default=None)
    dt: str | None = Field(default=None)