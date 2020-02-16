from db import db
from models.store import StoreModel


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # store_id column of the Item model (table) which is a foreign key to 'Stores' table
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    # Creates a object which retrieves all the related stores for a given Item.
    store = db.relationship('StoreModel')


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price, "store": self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name = <name> LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    '''
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(name=name).first()  # SELECT * FROM items WHERE name = <name> LIMIT 1

        :param name: 
        :return: 
                conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "SELECT * FROM ITEMS WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        # Return the item
        if row:
            return cls(row[1], row[2])
    '''

    '''
    def insert(self):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "INSERT INTO items VALUES(NULL, ?, ?)"
        cursor.execute(query, (self.name, self.price))

        conn.commit()
        conn.close()
    '''

    '''
    def update(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (self.price, self.name))

        conn.commit()
        conn.close()
    '''

    '''
    def delete(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (self.name,))

        conn.commit()
        conn.close()
    '''

