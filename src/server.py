from flask import Flask
from flask_restful import Resource, Api
from api.healthcheck import Healthcheck

app = Flask(__name__)
api = Api(app)

api.add_resource(Healthcheck, '/')

if __name__ == '__main__':
    app.run(debug=True)