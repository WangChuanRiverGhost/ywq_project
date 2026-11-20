from fastapi import APIRouter
from schemas.user import UserBase,UserCreate, UserLogin

router = APIRouter(prefix="/users", tags=["用户"])

@router.post("/users")
def create_user(user: UserCreate):
    pass

@router.post("/users/login")
def login_user(user: UserLogin):
    pass