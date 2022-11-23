import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404,message = "Store not found")

    item_id = uuid.uuid4.hex
    item = {**item_data, "id": item_id}
    items[item_id] = item 

    return new_item, 201


@app.get("/item/<string:store_id>")
def get_store():
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message = "Store not found")
    






