from sqlalchemy.orm import Session
from models.user import User
from schemas.users import UserCreate
from utils import verify_password

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(
        username=user.username,
        email = user.email,
        phone_number = user.phone_number,
        password = hashed_password
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception:
        pass 
    

def all_users(db: Session):
    return db.query(User).all()

def authenticate(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    print(user)
    if user is None:
        return None
    
    if not verify_password(password, user.password):
        return None

    return user

