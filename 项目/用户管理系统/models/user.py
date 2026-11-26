from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    
    __tablename__ = "users"  # 表名

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column[int](Integer,unique=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

