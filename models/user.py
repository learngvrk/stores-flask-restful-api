from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def fetch_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # SELECT * FROM users WHERE username=<username>

    @classmethod
    def fetch_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # SELECT * FROM users WHERE id = <_id>

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    '''
    @classmethod
    def fetch_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        # Query to pull user from DB
        query = "select * from users where id=?"
        cursor.execute(query, (_id,))
        result = cursor.fetchone()

        if result:
            # user = cls(result[0], result[1], result[2])
            user = cls(*result)
        else:
            user = None

        # Close the connection to the DB
        connection.close()
        return user
    '''

    '''
    @classmethod
    def fetch_by_username(cls, username):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            # Query to pull user from DB
            query = "select * from users where username=?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                # user = cls(result[0], result[1], result[2])
                user = cls(*result)
            else:
                user = None

            # Close the connection to the DB
            connection.close()
            return user
            '''