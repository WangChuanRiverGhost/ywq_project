from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

'''数据类的创建'''

# 基类
class UserBase(BaseModel):
    username: str

# 创建用户 注册
class UserCreate(UserBase):
    password: str
    email: Optional[str] = None

# 登录
class UserLogin(UserBase):
    password: str

# 存数据库
class UserInDB(UserBase):
    id: int
    hashed_password: str
    email: Optional[str] = None

'''应用的创建'''
app = FastAPI()
user = {}

@app.post("/register")
def create_user(register: UserCreate):
    user[register.username] = register.password
    return register.username

@app.post("/login")
def login_user(login: UserLogin):
    for key,value in user.items:
        if login.username == key and login.password == value:
            return {"message":"登录成功"}
        else:
            continue
    return {"message":"用户名或密码错误"}

# cursor新增后版本：
from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

'''数据类的创建'''

# 基类
class UserBase(BaseModel):
    username: str

# 创建用户 注册
class UserCreate(UserBase):
    password: str
    email: Optional[str] = None

# 登录
class UserLogin(UserBase):
    password: str

# 存数据库
class UserInDB(UserBase):
    id: int
    hashed_password: str
    email: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

'''应用的创建'''
app = FastAPI()
user = {}

@app.post("/register")
def create_user(register: UserCreate):
    user[register.username] = register.password
    return register.username

@app.post("/login")
def login_user(login: UserLogin):
    for key, value in user.items():
        if login.username == key and login.password == value:
            return {"message": "登录成功"}
        else:
            continue
    return {"message": "用户名或密码错误"}