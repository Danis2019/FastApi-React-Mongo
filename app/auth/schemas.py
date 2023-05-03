from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    telegramID: int
    password: str