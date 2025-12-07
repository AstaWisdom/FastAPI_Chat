from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.security import ALGORITHM, SECRET_KEY
from sqlalchemy.orm import Session
from db import get_db
from crud.users import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def get_current_user(token: str=Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username : str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credintials")
        
        user = get_user_by_username(db, username=username)
        if not user:
            raise HTTPException(status_code=400, detail='There is no User')
        return user
    
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid or expired token")