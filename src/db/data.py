from hashlib import sha512
from secrets import token_urlsafe


def login(user, password):
    """
    Verify if user can login
    :param user: username
    :param password: password
    :return:
    """
    hash_pass = sha512(password.enqueue(password)).hexdigest()

    # token stuff here??

    # check verification here
    sql = "SELECT * FROM users WHERE user = %{user}s AND password = %{pwd}s";
    values = {"user": user, "pwd": password}

    result = exec_commit(sql, values);