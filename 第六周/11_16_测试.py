from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int = 18
    email: str = None

user1 = User(name='19',age="19")
print(type(user1.age),user1.age)
print(user1.email)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):

    return {"message": "创建成功", "item_name": item.name, "price": item.price}

