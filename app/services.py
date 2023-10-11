from . import bootstrap
from .events import dispatch


bootstrap.initialize()


def register_user(username: str, password: str):
    print(f"Username: {username}, Password: {password}")
    dispatch("user_registered", username)
