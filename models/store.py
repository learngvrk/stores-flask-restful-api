from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Creates an object which retrieves all related items for a given Store
    # Since an object will be created when each Store (instance) is created, which is a costly operation, memory heavy
    # it can be avoided using another function parameter 'lazy'
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # self.items.all() is required only when the 'lazy' fn parameter is used, otherwise items.all is sufficient.
        # self.items becomes just a Query builder in this case.
        # Until we call the .json() method, the items object is not created, it is lazy,
        # object not created until one of its method is called (.json method, in this case)
        # this is a trade-off between speed of creation or speed of reading/calling the json method.
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM stores WHERE name = <name> LIMIT 1


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()