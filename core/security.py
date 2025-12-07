from dotenv import load_dotenv
from jose import jwt
from datetime import timedelta, datetime
import os

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30


def create_token_access(data: dict, expire_time: timedelta | None = None):
    to_encode = data.copy()

    expire = datetime.utcnow() + (expire_time or timedelta(minutes=TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp':expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
