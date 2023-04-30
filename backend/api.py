from typing import Union

from fastapi import FastAPI , Body

from main import *

app = FastAPI()


@app.get("/")
def read_root():
    return 'Website'

@app.post("/productcatalog/product" , tags=['Product'])
async def add_product(product_data:dict = Body(...)):
    new_product = Product(product_data.get("name"),product_data.get("price"),product_data.get("overview"),product_data.get("quantity"),product_data.setdefault("promotion_price",None))
    data = catalog.add_product(new_product)
    if new_product and data:
        return {"message":"Complete","catalog":data}
    else:
        return {"message":"Failed"}

@app.delete("/productcatalog/" , tags=['Product'])
async def remove_product(product_data:dict = Body(...)):
    try:
        return catalog.remove_product(product_data.get("product_id"))
    except:
        return 'Cant remove product'
    
@app.get("/productcatalog/{name}" , tags=['Product'])
async def search_product(name : str):
    return catalog.search_product(name)
    
@app.post("/account" , tags=['Account'])
async def create_account(account_data:dict = Body(...)):
    new_account , cart = accountlist.register(account_data.get("username"),account_data.get("password"),account_data.get("check_password"),account_data.get("email"),account_data.get("name"))
    data = accountlist.add_account(new_account)
    if data:
        return {"account" : new_account , "cart" : cart}
    else:
        return 'Failed'
    
@app.get("/account" , tags=['Account'])
async def login(username,password):
    try:
        account =  accountlist.login(username,password)
        return account , account.cart
    except:
        return 'Your username or password is wrong'
    
@app.post("/cart" , tags=['Cart'])
async def add_product_to_cart(item_data:dict = Body(...)):
    for product in catalog.products:
        if product.product_id == item_data.get("product_id"):
            return cart2.add_product_to_cart(product,item_data.get("quantity"))
        
@app.delete("/cart" , tags=['Cart'])
async def remove_product_from_cart(item_data:dict = Body(...)):
    for product in catalog.products:
        if product.product_id == item_data.get("product_id"):
            return cart2.remove_product_from_cart(product)
        
@app.post("/reviews" , tags=['Review'])
async def add_review(review_data:dict = Body(...)):
    for product in catalog.products:
        if product.product_id == review_data.get("product_id"):
            new_review = Review(review_data.get("rating"),review_data.get("name"))
            product.add_review(new_review)
            return product
        
@app.delete("/reviews" , tags=['Review'])
async def remove_review(review_data:dict = Body(...)):
    for product in catalog.products:
        if product.product_id == review_data.get("product_id"):
            product.remove_review(review_data.get("review_id"))
            return product