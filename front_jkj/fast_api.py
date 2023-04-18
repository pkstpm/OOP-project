from typing import Optional
from fastapi import FastAPI
from Accountlist import *

app=FastAPI()

Account_List = Accountlist()

#POST

@app.post("/sign_up", tags=["Account"])
async def create_account(task: dict) -> dict:
    
    data_return = Account_List.create_account(task["username"],task["password"],task["check_password"],task["email"],task["name"])
    
    return {
        "result" : data_return
    } #sign_up
    
@app.post("/login", tags=["Account"])
async def login(task: dict) -> dict:
    
    data_return = Account_List.login(task["username"],task["password"])
    
    return {
        "result" : data_return
    }#login

#GET

@app.get("/account_list", tags=["Account"])
async def get_Account_list() -> dict:
    list = Account_List.get_Account_list()
    return {"data": list}#account_list