from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "你好，这是我的第一个接口"}

@app.get("/hello")
def read_hello():
    return {"message": "你好，世界"}

@app.get("/about")
def read_about():
    return {"version": "1.0", "author": "你的名字"}