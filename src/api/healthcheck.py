from flask_restful import Resource, reqparse

class Healthcheck(Resource):
    def get(self):
        return {"ping": "pong"}
