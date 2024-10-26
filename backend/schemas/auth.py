from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    token: str


class AuthBase(BaseModel):
    email: EmailStr
    password: str


class RegisterInfo(AuthBase):
    fio: str


class LoginInfo(AuthBase):
    pass
