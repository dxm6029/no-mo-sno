from flask import Flask
from flask_restful import Resource, Api

from api.healthcheck import Healthcheck
from api.login import Login
from api.register import Register
from api.comments import Comments
from api.getComments import getComments
from api.getJobs import getJobs
from api.addJobs import addJobs
from api.getJobInfo import getJobInfo


app = Flask(__name__)
api = Api(app)

api.add_resource(Healthcheck, '/')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Comments, '/comments')
api.add_resource(getComments, '/comments/<id>')
api.add_resource(getJobs, '/jobs')
api.add_resource(addJobs, '/jobs')
api.add_resource(getJobInfo, '/jobInfo')



if __name__ == '__main__':
    app.run(debug=True)