from datetime import datetime, timezone, timedelta
from uuid import UUID
import jwt

from app.core.config import jwt_settings

def create_access_token(data: dict, expiry: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expiry:
        expire = datetime.now(timezone.utc) + expiry
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_settings.secret_key, algorithm=jwt_settings.algorithm)
    return encoded_jwt

def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, jwt_settings.secret_key, algorithms=[jwt_settings.algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        return None