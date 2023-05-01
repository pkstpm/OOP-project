from fastapi import FastAPI , Body
from main import *

app = FastAPI()

#search product
@app.get("/product/search_product/{name}")
async def search_by_name(name : str):
    return product_catalog.search_product_by_name(name)

#search by category
@app.get("/product/{category}/search_product/{name}")
async def search_by_category(name : str , category : str):
    return product_catalog.search_product_by_category(name,category)

#view_catalog
@app.get("/product")
async def view_catalog():
    return product_catalog.products

#view_product
@app.get("/product/{product_id}")
async def view_product(product_id : int):
    return product_catalog.get_product(product_id)

# view_category
@app.get("/{category}")
async def view_category(category : str):
    return product_catalog.get_by_category(category)

# login
@app.post("/login")
async def login(account_data:dict = Body(...)):
    try:
        account = account_list.verify_login(account_data.get("username"),account_data.get("password"))
        if account:
            return {"message":"Login success","account":account}
        else:
            return {"message":"Failed to login"}
    except:
        return {"message":"Failed"}
    
# register
@app.post("/register")
async def register(account_data:dict = Body(...)):
    try:
        if account_list.verify_account(account_data.get("username"),account_data.get("email")) == True:
            if account_list.check_password(account_data.get("password"),account_data.get("check_password")) == True:
                new_account = Customer(account_data.get("username"),account_data.get("password"),account_data.get("email"),account_data.get("name"))
        data = account_list.add_account(new_account)
        if new_account and data:
            return {"message":"Success","account":new_account}
    except:
        return {"message":"Failed"}

# view_cart
@app.post("/cart/")
async def view_cart(account_data:dict = Body(...)):
    account = account_list.get_account(account_data.get("account_id"))
    cart = account.cart
    return cart.view_cart()

# add_product_to_cart
@app.post("/cart/add_item")
async def add_product_to_cart(data:dict = Body(...)):
    try:
        account = account_list.get_account(data.get("account_id"))
        product = product_catalog.get_product(data.get("product_id"))
        cart = account.cart
        return cart.add_product_to_cart(product,data.setdefault("quantity",1))
    except:
        return 'Failed'

# add_review
@app.post("/product/review/add_review")
async def add_review(data:dict = Body(...)):
    try:
        account = account_list.get_account(data.get("account_id"))
        product = product_catalog.get_product(data.get("product_id"))
        new_review = Review(data.get("rating"),account.name)
        check = product.add_review(new_review)
        if check:
            return {"message":"Success","review":new_review}
    except:
        return {"message":"Failed"}
    
@app.post("/product/review")
async def view_review(product_data:dict = Body(...)):
    product = product_catalog.get_product(product_data.get("product_id"))
    return product.view_review()
        