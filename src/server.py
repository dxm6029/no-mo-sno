from flask import Flask
from flask_restful import Resource, Api
from api.healthcheck import Healthcheck, Help


app = Flask(__name__)
api = Api(app)

api.add_resource(Healthcheck, '/')
api.add_resource(Help, '/help/<id>')
'/help/id'


if __name__ == '__main__':
    app.run(debug=True)