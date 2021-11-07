from flask_restful import Resource
from db.data import getIdFromToken, getAllComments
from flask import request
from api.utils import authorization


class getComments(Resource):
    def get(self, id):
        test = authorization()
        if test is False:
            return "error user not authenticated "
        commentList = getAllComments(id)

        return {"comments": commentList}, 200





