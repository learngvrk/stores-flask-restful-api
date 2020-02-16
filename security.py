from models.user import UserModel


def authenticate(username, password):
    user = UserModel.fetch_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.fetch_by_id(user_id)
