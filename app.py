from flask import Flask

app = Flask(__name__)

stores = [
    { 
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


#@app.route("/")
@app.get("/store")
def get_stores():
    return {"stores": stores}
