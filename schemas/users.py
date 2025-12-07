from pydantic import BaseModel, EmailStr, Field, validator
import re



class UserCreate(BaseModel):
    username : str = Field(..., min_length=3, max_length=50)
    phone_number : str | None = None
    password: str = Field(..., min_length=8, max_length=72)
    email : EmailStr | None = None

    @validator("phone_number")
    def valid_phone(cls, v):
        if v is None:
            return v
        
        pattern = r"^(?:\+98|0)9\d{9}$"

        if not re.match(pattern, v):
            raise ValueError('This Phone Number Is not Valid')
        
        return v


class UserRead(BaseModel):
    id : int
    username : str
    phone_number : str | None = None
    email : EmailStr | None = None


class LoginRequest(BaseModel):
    username : str
    password : str