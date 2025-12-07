from fastapi import APIRouter , Depends, HTTPException
from schemas.users import UserCreate, UserRead, LoginRequest
from crud.users import create_user, get_user_by_username, all_users, authenticate
from db import get_db
from sqlalchemy.orm import Session
from utils import hashing_password
from core.security import create_token_access
from auth import get_current_user

router = APIRouter()


@router.post('/create_user', response_model = UserRead)
def user_create(user: UserCreate , db : Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail='This Username Is Already Exists')


    hash_password = hashing_password(user.password)
    user = create_user(db=db, user=user, hashed_password=hash_password)
    if not user:
        raise HTTPException(status_code=400, detail="This Email Is Already Exists")
    return user
    
@router.get('/users', response_model=list[UserRead])
def users(db: Session = Depends(get_db)):
    return all_users(db)


@router.post('/login')
def login(payload : LoginRequest, db : Session = Depends(get_db)):
    user = authenticate(db, payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=400, detail='No Username Exists')
        
    access_token = create_token_access({"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get('/token')
def testing(current_user=Depends(get_current_user)):
    return {'username':current_user}