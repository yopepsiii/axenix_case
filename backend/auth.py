from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_password_bearer_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_auth_headers(token: str = Depends(oauth2_password_bearer_scheme)):
    headers = {"bearerAuth": token}
    return headers
