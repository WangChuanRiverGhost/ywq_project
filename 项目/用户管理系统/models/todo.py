from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=True) 