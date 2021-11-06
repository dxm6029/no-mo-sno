from hashlib import sha512
from secrets import token_urlsafe

from db.utils import exec_commit, exec_commit_return, exec_get_one


def login(user, password):
    """
    Verify if user can login
    :param user: username
    :param password: password
    :return: token if authenticated, none if not
    """
    hash_pass = sha512(password.encode("utf-8")).hexdigest()

    # token stuff here
    token = token_urlsafe(16)

    # check verification here
    sql = "UPDATE users SET token = %(tok)s WHERE username = %(usr)s AND hashed_password = %(pwd)s"
    values = {"tok": token, "usr": user, "pwd": hash_pass}

    result = exec_commit(sql, values)

    if(result > 0):
        return token

    return None

def register(user, password, fname, lname, location):
    """

    :param user:
    :param password:
    :param fname:
    :param lname:
    :param location:
    :return: if inserted successfully
    """
    hash_pass = sha512(password.encode("utf-8")).hexdigest()

    sql = "INSERT INTO USERS(fname, lname, username, hashed_password, location) VALUES (%(fname)s, %(lname)s, %(username)s, %(hashed_password)s, %(location)s)"
    values = {"fname": fname, "lname": lname, "username": user, "hashed_password": hash_pass, "location": location}

    result = exec_commit(sql, values)

    if(result > 0):
        return True
    else:
        return False

def getIdFromToken(token):
    """

    :param token:
    :return: user id
    """
    sql = "SELECT id FROM users WHERE token=%(tok)s"
    values = {"tok": token}

    result = exec_get_one(sql, values)
    return result[0]

if __name__ == '__main__':
    #login("dmolee", "pass123")
    print(getIdFromToken("FDx1b2FNa1kvlz92jvgMbw"))


