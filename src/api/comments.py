# get the user of the one commenting and the one that your commenting about
from flask_restful import Resource, reqparse
from db.data import getIdFromToken, createComment
from flask import request

class Comments(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("targetUser", type=str)
        parser.add_argument("comments", type=str)

        args = parser.parse_args()
        targetUser = args["targetUser"]
        comments = args["comments"]

        token = request.headers.get('token')

        postUser = getIdFromToken(token)
        works = createComment(postUser, targetUser, comments)

        if works is False:
            return "Comment inserted failed", 400
        return "comment posted", 200


