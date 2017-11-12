from flask_bcrypt import check_password_hash
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and check_password_hash(user.pw_hash, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
