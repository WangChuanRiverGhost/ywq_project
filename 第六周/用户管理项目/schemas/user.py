from pydantic import BaseModel
from typing import Optional

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