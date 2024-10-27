from config import settings


async def get_auth_headers():
    headers = {"bearerAuth": settings.axenix_api_key}
    return headers
