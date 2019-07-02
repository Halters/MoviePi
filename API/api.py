#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## api_gateway
## File description:
## api.py
##

from flag import Flag
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from flask_api import status
from Users import Users
from Username import Username
from User import User
from Genres import Genres
import json
import hashlib
import jwt
import uuid
import time

app = Flask(__name__)
api = Api(app)
CORS(app)

#class User(Resource):
#    def post(self):
#        packet = request.json
#
#    ##def get(self, command):
#
#    ##def update(self, command):



api.add_resource(Users, '/api/v1/users') # Route_1 // TYPE = POST
api.add_resource(Username, '/api/v1/checkUsername') # Route 2 // Type = GET
api.add_resource(User, '/user/register') # Route 2 // TYPE = POST
api.add_resource(Genres, '/api/v1/genres')
#api.add_resource(User, '/user/<id>') # Route 3 // TYPE = GET
#api.add_resource(User, '/user/<id>') # Route 4 // TYPE = UPDATE
if __name__ == '__main__':
     app.run(host='0.0.0.0', port='4242')