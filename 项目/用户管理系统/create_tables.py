from database import Base, engine
from models import User, Todo

Base.metadata.create_all(bind=engine)
print("✅ 表创建成功！")