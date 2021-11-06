from hashlib import sha512
from secrets import token_urlsafe
from db.utils import exec_commit


def login(user, password):
    """
    Verify if user can login
    :param user: username
    :param password: password
    :return: token if authenticated, none if not
    """
    hash_pass = sha512(password.enqueue(password)).hexdigest()

    # token stuff here
    token = token_urlsafe(16)

    # check verification here
    sql = "UPDATE users SET token = %{tok}s WHERE user = %{usr}s AND password = %{pwd}s"
    values = {"tok": token, "usr": user, "pwd": hash_pass}

    result = exec_commit(sql, values)

    if(result > 0):
        return token

    return None


