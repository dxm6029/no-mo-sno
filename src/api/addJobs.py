import requests
from flask_restful import Resource, reqparse
from db.data import addJob


class addJobs(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("customerID", type=str)
        parser.add_argument("workerID", type=str)
        parser.add_argument("location", type=str)
        parser.add_argument("price", type=str)
        parser.add_argument("rating", type=str)
        args = parser.parse_args()
        customerID = args["customerID"]
        workerID = args["workerID"]
        location = args["location"]
        price = args["price"]
        rating = args["rating"]

        work = addJob(customerID, workerID, location, price, rating)
        if work is False:
            return "Job not inserted", 400
        return "succeeded", 200
