from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/user_management_db?charset=utf8mb4",
    echo=True,
    pool_size=5,
    max_overflow=10
)
