from flask_restful import Resource
from db.data import getIdFromToken, getAllComments
from flask import request


class getComments(Resource):
    def get(self, id):
        token = request.headers.get('token')
        postUser = getIdFromToken(token)
        if postUser is None:
            return "error user not authenticated "
        commentList = getAllComments(id)

        return {"comments": commentList}, 200





