from hashlib import sha512
from secrets import token_urlsafe

from db.utils import exec_commit, exec_commit_return, exec_get_one, exec_get_all


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

    if result is None:
        return None

    return result[0]

def getUserInfoFromId(id):
    """

    :param token:
    :return: user id
    """
    sql = "SELECT fname, lname, username, location, shovel_rating, num_shovel_rating, house_rating, num_house_rating FROM users WHERE id=%(id)s"
    values = {"id": id}

    result = exec_get_all(sql, values)

    dictList = []

    for data in result:
        dictList.append({"fname": data[0], "lname": data[1], "username": data[2], "location": data[3], "shovelRating": data[4], "numShovelRating": data[5], "houseRating": data[6], "numHouseRating": data[7]})

    return dictList

def createComment(postUser, targetUser, comment):
    """

    :param customerID:
    :param workerID:
    :param postUser:
    :param comment:
    :return:
    """

    sql = "INSERT INTO comments(postUser, targetUser, description) VALUES (%(postUser)s, %(targetUser)s, %(description)s)"
    values = {"postUser": postUser, "targetUser": targetUser, "description": comment}

    result = exec_commit(sql, values)

    if (result > 0):
        return True
    else:
        return False

def getAllComments(id):
    """

    :param id:
    :return: if they are worker or cusotmer and they did not post it
    """

    sql = "SELECT c.commentId, ut.username as postUser, u.username as targetUser, c.description FROM comments c JOIN users u on c.targetUser = u.id JOIN users ut on c.postUser = ut.id WHERE c.targetUser =%(targetUser)s "
    values = {"targetUser": id}

    result = exec_get_all(sql, values)

    dictList = []

    for data in result:
        dictList.append({"commentId": data[0], "postUser": data[1], "username": data[2], "description":data[3]})

    return dictList

if __name__ == '__main__':
    print(getUserInfoFromId(2))


