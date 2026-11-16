from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}

@app.get("/search")
def get_search(q:str,page:int=1):
    return {"q":q,"page":page}