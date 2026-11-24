from hmac import new
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter,HTTPException,Depends, Header
from passlib.context import CryptContext
import hashlib,jwt

from schemas.user import UserBase,UserCreate, UserLogin

class LengthPasswordError(HTTPException):
    pass

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your-secret-key-keep-it-safe"   # 配置密钥
ALGORITHM = "HS256" # 配置算法
# 创建JWT
def create_access_token(user_id: int, expires_minutes: int = 30) -> str: # 生成JWT
    payload = {
        "sub": str(user_id), # 用户ID
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_minutes), # 过期时间
        "iat": datetime.now(timezone.utc), # 签发时间（可选）
    }
    token = jwt.encode(payload, SECRET_KEY,algorithm=ALGORITHM)

    return token
# 验证JWT是否为期望值
def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token 已过期")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="token 无效")
# 检查客户端是否传入token，是则进行校验，校验通过则返回用户id
def get_current_user(authorization: str = Header(None)) -> int: # 如果没有返回异常则返回用户id
    if not authorization or not authorization.startswith("Bearer "): # 检查客户端是否传入token
        raise HTTPException(status_code=401, detail="缺少 token")
    token = authorization.removeprefix("Bearer ")
    payload = decode_token(token)
    return int(payload["sub"])

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
    hashed = pwd_context.hash(user.password)
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

    # 查找用户名
    found = next((u for u in users_db if u["username"] == user.username), None)

    # 验证是否存在该用户
    if not found:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    # 验证密码是否和加密后相同
    if not pwd_context.verify(user.password, found["hashed_password"]):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    
    token = create_access_token(found["id"])
    # 返回token
    return {"message": "登录成功", "username": user.username,"access_token": token, "token_type": "bearer"}

@router.get(f"/my-account")
def read_me(user_id: int = Depends(get_current_user)): # 依赖函数
    return {"user_id": user_id}