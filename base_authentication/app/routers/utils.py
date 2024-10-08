import jwt
from fastapi import HTTPException

from services.auth import JWT_SECRET_KEY, JWT_SECRET_ALGORITHM


def verify_autorization_header(access_token: str):
    if not access_token or not access_token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No auth provided.")

    try:
        token = access_token.split("Bearer ")[1]
        auth = jwt.decode(token, JWT_SECRET_KEY, JWT_SECRET_ALGORITHM)
    except jwt.InvalidTokenError as err:
        raise HTTPException(status_code=401, detail=f"Invalid token.")

    return auth
