from flask_restful import Resource, Api, reqparse
from models.user import UserModel


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Mandatory Field')
    parser.add_argument('password', type=str, required=True, help='Mandatory Field')

    @classmethod
    def post(cls):

        request = UserRegistration.parser.parse_args()

        if UserModel.fetch_by_username(request['username']):
            return {"message": "User with the username: {} already exists".format(request['username'])}, 400
        else:
            new_user = UserModel(request['username'], request['password'])
            new_user.save_to_db()

    '''
            # Create a connection to DB
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            query = "INSERT INTO users VALUES(NULL, ?, ?)"
            cursor.execute(query, (request['username'], request['password']))

            connection.commit()
            connection.close()

            return {"message": "User Registration Completed"}, 201
    '''


