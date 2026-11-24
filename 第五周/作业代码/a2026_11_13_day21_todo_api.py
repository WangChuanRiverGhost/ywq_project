from fastapi import FastAPI
from pydantic import BaseModel

todo_list = FastAPI()

class todo_text(BaseModel):
    title:str
    status:bool