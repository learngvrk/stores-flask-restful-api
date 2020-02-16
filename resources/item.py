from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel
from sqlalchemy import exc


class Item(Resource):
    # Add a parser
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This is a mandatory field')

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Needs a associated store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):  # {"price": <price>, "store": <store_id>}
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': "An store with name '{}' already exists.".format(name)}, 400
        request = Item.parser.parse_args()
        new_item = ItemModel(name, **request)

        # Insert record function
        try:
            new_item.save_to_db()
        except exc.SQLAlchemyError as e:
            return {"message": "There was a unexpected error inserting the store: {}".format(e)}, 500

        return new_item.json(), 201


    @jwt_required()
    def delete(self, name):
        # Retrieve the item from ItemsList
        item = ItemModel.find_by_name(name)
        if item:
            try:
                item.delete_from_db()
            except exc.SQLAlchemyError as e:
                return {"message": "There was an error deleting the store: {}".format(e)}, 500
        else:
            return {"message": "Store not found"}, 404

        return item.json(), 201

    @jwt_required()
    def put(self, name):  # {"price": <price>, "store": <store_id>}
        request = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            # Create item with price and store id
            item = ItemModel(name, **request)
        else:
            # Update the existing item price and store id
            item.price = request['price']
            item.store_id = request['store_id']

        # Insert record function
        try:
            item.save_to_db()
        except:
            return {"message": "There was a unexpected error inserting the store"}, 500

        return item.json(), 201


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
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