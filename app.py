from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegistration
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# Create the Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "jsn"

# Create the Api and pass the Flask Application
api = Api(app)


# Create a JSON Web Token
jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(Item, '/item/<string:name>')               # http://127.0.0.1:5000/item/chair
api.add_resource(ItemList, '/items')                        # http://127.0.0.1:5000/items
api.add_resource(UserRegistration, '/UserRegistration')     # http://127.0.0.1:5000/UserRegistration
api.add_resource(Store, '/store/<string:name>')             # http://127.0.0.1:5000/store
api.add_resource(StoreList, '/stores')

# Execute the App run function only if we run the app.py directly and not when app.py is imported from another
# module or class
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)