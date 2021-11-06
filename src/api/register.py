import requests
from flask_restful import Resource, reqparse
from db.data import register


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("firstName", type=str)
        parser.add_argument("lastName", type=str)
        parser.add_argument("location", type=str)

        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        firstName = args["firstName"]
        lastName = args["lastName"]
        location = args["location"]

        insert = register(username, password, firstName, lastName, location)

        if insert is False:
            return "Wrong table data", 400
        return "success", 200
