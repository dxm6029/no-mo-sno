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

def addJob(customerId, workerId, location, price, rating):
    """

    :param user:
    :param password:
    :param fname:
    :param lname:
    :param location:
    :return: if inserted successfully
    """

    sql = "INSERT INTO jobs(customerId, workerId, location, price, rating) VALUES (%(customerId)s, %(workerId)s, %(location)s, %(price)s, %(rating)s)"
    values = {"customerId": customerId, "workerId": workerId, "location": location, "price": price, "rating": rating}

    result = exec_commit(sql, values)

    if(result > 0):
        return True
    else:
        return False

# as a worker, i want to see all the jobs available to me = sorting by rating
def getJob():
    sql = "SELECT u.username AS customerID, ut.username AS workerID, jobs.location, price, rating FROM jobs JOIN users " \
          "AS u ON u.id=jobs.customerid JOIN users AS ut ON ut.id=jobs.workerid ORDER BY rating DESC"
    result = exec_get_all(sql, None)
    dictList = []

    for data in result:
        dictList.append({"customerID": data[0], "workerID": data[1], "location": data[2], "price": data[3],
                         "rating": float(str(data[4]))})
    return dictList

def filteredGetJobs(available: bool=False, location: str=None):
    """

    :param available: boolean to indicate if we only want open jobs
    :param location: city
    :return:
    """
    sql = "SELECT u.username AS customerID, ut.username AS workerID, jobs.location, price, rating FROM jobs JOIN " \
          "users AS u ON u.id=jobs.customerid JOIN users AS ut ON ut.id=jobs.workerid"
    end_sql = " ORDER BY rating DESC"
    condition_sql = ""
    first_condition = True
    values = {}
    if available:
        condition_sql += " WHERE jobs.status LIKE %(status)s"
        values["status"] = "pending"
        first_condition = False
    if location:
        if first_condition:
            condition_sql += " WHERE "
        else:
            condition_sql += " AND "
        condition_sql += "jobs.location LIKE %(location)s"
        values["location"] = f"%{location}%"

    result = exec_get_all(sql + condition_sql + end_sql, values)
    dict_list = []

    for data in result:
        dict_list.append({"customerID": data[0], "workerID": data[1], "location": data[2], "price": data[3],
                         "rating": float(str(data[4]))})
    return dict_list


if __name__ == '__main__':
    print(filteredGetJobs(True, "Rochester"))


