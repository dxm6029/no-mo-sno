from flask_restful import Resource, reqparse
from db.data import updateStatusToPending, updateStatusToComplete, updateStatusToInProgress
from flask import request
from api.utils import authorization


class changeStatus(Resource):
    def put(self, id):
        test = authorization()
        if test == False:
            return "error user not authenticated"

        parser = reqparse.RequestParser()
        parser.add_argument("updateTO", type=str)
        args = parser.parse_args()
        updateTO = args["updatTO"]

        if updateTO == 'Pending':
            updateStatusToPending(id)
        if updateTO == 'InProgress':
            updateStatusToInProgress(id)
        if updateTO == 'Complete':
            updateStatusToComplete(id)

        return "Job Status Updated", 200
