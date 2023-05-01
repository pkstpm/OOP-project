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
    return product_catalog.view_catalog()

