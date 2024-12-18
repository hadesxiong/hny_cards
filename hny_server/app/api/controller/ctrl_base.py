# coding=utf8

from app.models.user import GuestMain
from app.utils.security import create_token, get_guest
from app.core.config import settings
from app.core.error import CustomHTTPException

# 定义游客登陆
async def login_guest_handler(finger: str | None = None):

    if finger:

        guest_id = await get_guest(GuestMain, finger)
        token_data = create_token({'guest': guest_id[6:]})
        return token_data
    
    else:
        raise CustomHTTPException(status_code=400, detail='数据不合法', err_code=40014)