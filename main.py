
from fastapi import FastAPI
from fastapi import responses
from enum import Enum
import uvicorn

app = FastAPI()

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

resp = "This is a test"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message": "Deep "}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN"}
    
    return {"model_name": model_name, "message": "wutt"}



@app.get("/my-first-api")
def hello():
    return {"message":"hello world"}

@app.get("/get_test")
async def test():
    return {"message": resp}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return{"item_id":item_id}

@app.get("/users/me")
async def read_user_me():
    return{"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return{"user_id": user_id}

@app.put("/set_test/{s}")
def set_test(s):
    resp = s



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)