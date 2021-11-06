# get the user of the one commenting and the one that your commenting about
from flask_restful import Resource, reqparse
# from db.data import comments

class Comments(Resource):
    def post(self):







class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]

        token = login(username, password)
        if token is None:
            return "Wrong login", 400
        return {"token": token}, 200