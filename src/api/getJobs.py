from flask_restful import Resource
from db.data import getJob
from flask import request


class getJobs(Resource):
    def get(self):
        jobList = getJob()
        return {"jobs": jobList}, 200
