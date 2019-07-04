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
from UserGenres import UserGenres
from Suggestions import Suggestions

app = Flask(__name__)
api = Api(app)
CORS(app)

API_SUBURL = '/api'
API_VERSION = '1'

API_BASEURL = API_SUBURL + '/v' + API_VERSION + '/'

api.add_resource(Users, API_BASEURL + 'users')
api.add_resource(Username, API_BASEURL + 'checkUsername/<username>')
api.add_resource(User, API_BASEURL + 'user')
api.add_resource(UserGenres, API_BASEURL +
                 'user/genres/<uuid>', API_BASEURL +
                 'user/genres')
api.add_resource(Genres, API_BASEURL + 'genres')
api.add_resource(Suggestions, API_BASEURL + 'suggestions')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4242')
