from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):  # {"store": <store>}
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "A Store with name '{}' already exists.".format(name)}, 400
        # request = Store.parser.parse_args()
        new_store = StoreModel(name)
        # Insert record function
        try:
            new_store.save_to_db()
        except:
            return {"message": "There was a unexpected error inserting the store"}, 500

        return new_store.json(), 201

    @jwt_required()
    def delete(self, name):
        # Retrieve the item from ItemsList
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {"message": "There was an error deleting the store"}, 500
        else:
            return {"message": "Item not found"}, 404

        return store.json(), 201

    @jwt_required()
    def put(self, name):  # {"name": <name>}
        # request = Store.parser.parse_args()

        store = StoreModel.find_by_name(name)

        if store is None:
            # Update the existing item price
            store = StoreModel(name)
        #  else:
        #      item.price = request['price']

        store.save_to_db()
        return store.json(), 201


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
        # return {'items': [item.json() for item in ItemModel.query.all()]}

    '''
    @jwt_required()
    def get(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        rows = result.fetchall()
        conn.close()

        items = [{"name": row[1], "price": row[2]} for row in rows]
        return {"items": items}
    '''