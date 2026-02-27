from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str  # 'admin' or 'employer' or 'candidate'
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    
    class Config:
        orm_mode = True
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    
    class Config:
        orm_mode = True 
        
