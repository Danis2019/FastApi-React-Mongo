from fastapi import APIRouter
# app/auth/auth_handler.py

import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = "Your_secret_key"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(telegramID: str) -> Dict[str, str]:
    payload = {
        "telegramID": telegramID,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}