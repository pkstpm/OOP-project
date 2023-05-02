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
            if account.account_id == "admin":
                return {"message":"Login success","account":account,"role":"admin"}
            elif  isinstance(account.account_id,int):
                return {"message":"Login success","account":account,"role":"customer"}
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
    
# remove_product_from_cart
@app.put("/cart/remove_item/")
async def remove_product_from_cart(data:dict = Body(...)):
    try:
        account =  account_list.get_account(data.get("account_id"))
        cart = account.cart
        cart.remove_product_from_cart(data.get("product_id"))
        return cart
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

# view_review
@app.post("/product/review")
async def view_review(product_data:dict = Body(...)):
    product = product_catalog.get_product(product_data.get("product_id"))
    return product.view_review()

# make_order
@app.post("/make_order")
async def make_order(account_data:dict = Body(...)):
    account =  account_list.get_account(account_data.get("account_id"))
    return account.make_order()

# cancel order
@app.post("/cancel_order")
async def cencel_order(data:dict = Body(...)):
    account =  account_list.get_account(data.get("account_id"))
    account.cancel_order(data.get("order_id"))
    return account.cart

@app.post("/view_order/")
async def view_order(data:dict = Body(...)):
    account =  account_list.get_account(data.get("account_id"))
    order = account.get_order(data.get("order_id"))
    return order
        
# payment
@app.put("/payment")
async def payment(data:dict = Body(...)):
    account = account_list.get_account(data.get("account_id"))
    order = account.get_order(data.get("order_id"))
    if data.get("payment") == "Shoppay":
        account.add_history_purchase(order)
        account.orders.remove(order)
        return shoppay.pay(order)
    if data.get("payment") == "Paypal":
        account.add_history_purchase(order)
        account.orders.remove(order)
        return paypal.pay(order)
    if data.get("payment") == "Googlepay":
        account.add_history_purchase(order)
        account.orders.remove(order)
        return googlepay.pay(order)

# edit_profile
@app.put("/edit_profile")
async def edit_profile(account_data:dict = Body(...)):
    try:
        account =  account_list.get_account(account_data.get("account_id"))
        account.edit_profile(account_data.get("name"),account_data.get("address"))
        if account:
            return {"message":"edit profile success","account":account}
    except:
        return {"message":"failed to edit profile"}
    
@app.post("/view_history_purchase")
async def view_history_purchase(account_data:dict = Body(...)):
    account = account_data.get("account_id")
    return account.history_purchase