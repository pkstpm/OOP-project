from typing import Union
from fastapi import FastAPI
from main import *

app = FastAPI()


#search by product
@app.get("/search_name/{name}" , tags=["Product"])
def search_nameproduct(name:str):
    return catalog.search_product_by_name(name)

#search by category
@app.get("/search_category/{category}" , tags=["Product"])
def search_categoryproduct(category:str):
    return catalog.search_product_by_category(category)

#view catalog
@app.get("/view_catalog" , tags=["Product"])
def view_catalog():
    return catalog.view_catalog()

#get account list
@app.get("/account_list" , tags=["Account"])
def get_account_list():
    return account_list.get_account_list()

#sign up
@app.post("/sign_up", tags=["Account"])
def sign_up(username, password, check_password, email, name):
    new_account = account_list.create_account(username, password, check_password, email, name)
    return new_account

#login
@app.post("/login", tags=["Account"])
def login(username, password):
    account = account_list.login(username, password)
    return account