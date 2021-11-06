from hashlib import sha512
from secrets import token_urlsafe


def login(user, password):
    """
    Verify if user can login
    :param user: username
    :param password: password
    :return:
    """
    return "token"