import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class UserOuts(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime.datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime.datetime
    owner_id: int
    owner: UserOuts
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post:Post
    Votes: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class CreateUser(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)