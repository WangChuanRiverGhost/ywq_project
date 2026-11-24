from hmac import new
from fastapi import APIRouter
from fastapi import HTTPException
import hashlib
from schemas.user import UserBase,UserCreate, UserLogin

class LengthPasswordError(HTTPException):
    pass

router = APIRouter(prefix="/users", tags=["用户"])

users_db = []

@router.post("/users")
def create_user(user: UserCreate):
    # 重名校验
    if any(u["username"] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="用户名已存在")
    # 用户密码长度校验
    if len(user.password) >= 8 and len(user.password) <= 15:
        pass
    else:
        raise LengthPasswordError(status_code=400,detail="密码长度不符合要求,需要大于7位并小于16位")
    # 用户密码加密
    hashed = hashlib.sha256(user.password.encode()).hexdigest()
    # 设置用户id
    new_id = len(users_db)+1
    # 存入用户信息
    user_in_db = {
        "id": new_id,
        "username": user.username,
        "hashed_password": hashed,
        "email": user.email,
    }
    users_db.append(user_in_db)
    # 把信息返回给前端
    return {"id": new_id, "username": user.username}

@router.post("/users/login")
def login_user(user: UserLogin):
    pass