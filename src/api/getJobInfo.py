import requests
from flask_restful import Resource
from db.data import getIdFromToken, getAllComments, filteredGetJobs
from flask import request


class getJobInfo(Resource):
    def get(self):
        token = request.headers.get('token')
        postUser = getIdFromToken(token)
        if postUser is None:
            return "error user not authenticated"
        location = request.args.get('location')
        openJobInfo = filteredGetJobs(available=True, location=location)

        return {"openJobInfo": openJobInfo}, 200





