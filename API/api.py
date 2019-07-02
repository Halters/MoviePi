#!/usr/bin/env python3
##
# EPITECH PROJECT, 2018
# api_gateway
# File description:
# api.py
##

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from Users import Users
from Username import Username
from User import User
from Genres import Genres

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Users, '/api/v1/users')
api.add_resource(Username, '/api/v1/checkUsername/<username>')
api.add_resource(User, '/user/register')
api.add_resource(Genres, '/api/v1/genres')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4242')
