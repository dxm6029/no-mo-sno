import psycopg2
import yaml
import os
from dotenv import load_dotenv
from flask import request
from db.data import getIdFromToken

load_dotenv()


def authorization():
    token = request.headers.get('token')
    postUser = getIdFromToken(token)
    if postUser is None:
        # error user not authenticated
        return False
    if postUser is not None:
        return True
