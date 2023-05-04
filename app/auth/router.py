from fastapi import APIRouter, Body
import random
from .schemas import *
from .auth_handler import *
from .auth_bearer import JWTBearer
from ..config import TOKEN_AUTOCLICK
import requests
from ..connection import db
from fastapi.encoders import jsonable_encoder
router = APIRouter()

users = []

async def send_password_bot(chat_id, password):
    URL = f'https://api.telegram.org/bot{TOKEN_AUTOCLICK}'
    responce = requests.post(URL + "/sendMessage", data={"chat_id": chat_id, "text": f"Код для входа в autoclick: {password}", "parse_mode": "Markdown"})
    return responce

def check_user(data: UserLoginSchema):
    for user in users:
        print(user)
        if int(user["telegramId"]) == data.telegramID and user["password"] == data.password:
            return True
    return False


@router.post("/smscode", tags=["jwt"])
async def smscode(phone: str):
    phone = jsonable_encoder({phone})
    user = await db.users.find_one({"phone": phone[0]})
    if not user:
        return 'No user'
    else:
        password = random.randint(1000, 9999)
        await send_password_bot(user["telegramId"], password)
        users.append({"telegramId": user["telegramId"],
                       "password": password
                    })
        return 'User found'

@router.post("/jsonwebtokensms", tags=["jwt"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.telegramID)
    return {
        "error": "Wrong login details!"
    }