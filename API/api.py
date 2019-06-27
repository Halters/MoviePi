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
from sqlalchemy import create_engine
from flask_api import status
from json import dumps

app = Flask(__name__)
movie_connect = create_engine('mysql+pymysql://root:Sphinxdepau40@@localhost:3306/TMDB')
user_connect = create_engine('mysql+pymysql://root:Sphinxdepau40@@localhost:3306/ACCOUNT_BASE')
api = Api(app)

class User(Resource):
    def post(self):

    def patch(self, command):

    def get(self, command):

    def update(self, command):


class Users



api.add_resource(Users, '/users/login/') # Route_1 // TYPE = POST
api.add_resource(User, '/user/register/') # Route 2 // TYPE = POST
api.add_resource(User, '/user/<id>') # Route 3 // TYPE = PATCH
api.add_resource(User, '/user/<id>') # Route 4 // TYPE = GET
api.add_resource(User, '/user/<id>') # Route 5 // TYPE = UPDATE
if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')