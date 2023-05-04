from fastapi import FastAPI , Body
from main import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
@app.post("/cart")
async def view_cart(account_data:dict = Body(...)):
    account = account_list.get_account(account_data.get("account_id"))
    cart = account.cart
    item = cart.get_item()
    return {"item":item,"total_price":cart.calculate_total_price()}

# add_product_to_cart
@app.post("/cart/add_item")
async def add_product_to_cart(data:dict = Body(...)):
    account = account_list.get_account(data.get("account_id"))
    product = product_catalog.get_product(data.get("product_id"))
    cart = account.cart
    return cart.add_product_to_cart(product,data.setdefault("quantity",1))
    
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
        new_review = Review(data.get("rating"),account.name,account.account_id)
        check = product.add_review(new_review)
        if check:
            return {"message":"Success","review":new_review}
    except:
        return {"message":"Failed"}
    
#remove_review
@app.put("/product/review/remove_review")
async def remove_review(data:dict = Body(...)):
    product = product_catalog.get_product(data.get("product_id"))
    check = product.remove_review(data.get("review_id"),data.get("account_id"))
    if check:
        return {"message":"success"}
    

# view_review
@app.post("/product/review")
async def view_review(product_data:dict = Body(...)):
    product = product_catalog.get_product(product_data.get("product_id"))
    return product.view_review()

# make_order
@app.post("/make_order")
async def make_order(account_data:dict = Body(...)):
    account = account_list.get_account(account_data.get("account_id"))
    order = account.make_order()
    return {"data":order,"order_id":order.order_id}

# cancel_order
@app.post("/cancel_order")
async def cencel_order(data:dict = Body(...)):
    account =  account_list.get_account(data.get("account_id"))
    account.cancel_order(data.get("order_id"))
    return account.cart

# view_order
@app.get("/view_order/{account_id}/{order_id}")
async def view_order(order_id : int,account_id : int):
    account =  account_list.get_account(account_id)
    order = account.get_order(order_id)
    return {"item":order.view_order(),"total_price":order.total_price}
        
# payment
@app.put("/payment")
async def payment(data:dict = Body(...)):
    account = account_list.get_account(data.get("account_id"))
    order = account.get_order(data.get("order_id"))
    if data.get("payment") == "Shoppay":
        item = order.view_order()
        date = datetime.datetime.now()
        result = {"item":item,"total_price":order.total_price,"payment":order.payment,"name":account.name,"address":account.address,"pay_date":date.strftime("%x")}
        account.add_history_purchase(result)
        account.orders.remove(order)
        return shoppay.pay(order)
    if data.get("payment") == "Paypal":
        item = order.view_order()
        date = datetime.datetime.now()
        result = {"item":item,"total_price":order.total_price,"payment":order.payment,"name":account.name,"address":account.address,"pay_date":date.strftime("%x")}
        account.add_history_purchase(result)
        account.orders.remove(order)
        return paypal.pay(order)
    if data.get("payment") == "Googlepay":
        item = order.view_order()
        date = datetime.datetime.now()
        result = {"item":item,"total_price":order.total_price,"payment":order.payment,"name":account.name,"address":account.address,"pay_date":date.strftime("%x")}
        account.add_history_purchase(result)
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
    
# view_history_purchase
@app.get("/view_history_purchase/{account_id}")
async def view_history_purchase(account_id : int):
    account = account_list.get_account(account_id)
    return account.history_purchase

# create_product
@app.post("/create_product")
async def add_product(data:dict = Body(...)):
    category = data.get("category")
    if data.get("account_id") == "admin":
        if category == "keyboard":
            new_product = Keyboard(name = data.get("name"),
                                    price = data.get("price"),
                                    promotion_price = data.setdefault("promotion_price",None),
                                    overview = data.get("overview"),
                                    quantity = data.get("quantity"),
                                    keyboard_switch = data.get("keyboard_switch"),
                                    keyboard_keycap = data.get("keyboard_keycap"),
                                    keys = data.get("keys"),
                                    casecolor = data.get("casecolor"))
        elif category == "keycap":
            new_product = Keycap(name = data.get("name"),
                                    price = data.get("price"),
                                    promotion_price = data.setdefault("promotion_price",None),
                                    overview = data.get("overview"),
                                    quantity = data.get("quantity"),
                                    kit = data.get("kit"),
                                    profile = data.get("profile"),
                                    type_keycap = data.get("type_keycap"))
        elif category == "switch":
            new_product = Switch(name = data.get("name"),
                                    price = data.get("price"),
                                    promotion_price = data.setdefault("promotion_price",None),
                                    overview = data.get("overview"),
                                    quantity = data.get("quantity"),
                                    variation = data.get("variation"),
                                    spring_weight = data.get("spring_weight"),
                                    type_switch = data.get("type_switch"))
        elif category == None:
            new_product = Product(name = data.get("name"),
                                    price = data.get("price"),
                                    promotion_price = data.setdefault("promotion_price",None),
                                    overview = data.get("overview"),
                                    quantity = data.get("quantity"))
        data = product_catalog.add_product(new_product)
        if new_product and data:
            return {"message":"Success","product":new_product}
        
# remove_product
@app.put("/product/{product_id}")
async def remove_product(product_id:int):
    product = product_catalog.get_product(product_id)
    product_catalog.remove_product(product)
    return {"message":"Success"}

# view_all_order
@app.get("/view_all_order/{account_id}")
async def view_all_order(account_id : int):
    account = account_list.get_account(account_id)
    return account.orders