#!/usr/bin/env python3
##
# EPITECH PROJECT, 2018
# api_gateway
# File description:
# api.py
##

import sys
if __name__ == '__main__':
    sys.path.insert(0, '../')

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from moviepiapi.Users import Users
from moviepiapi.Username import Username
from moviepiapi.User import User
from moviepiapi.Genres import Genres
from moviepiapi.UserGenres import UserGenres
from moviepiapi.UserFilmsSeen import UserFilmsSeen
from moviepiapi.Suggestions import Suggestions
from moviepiapi.Films import Films
from moviepiapi.Actor import Actor
from moviepiapi.Directors import Directors


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
api.add_resource(UserFilmsSeen, API_BASEURL +
                 'user/filmsSeen')
api.add_resource(Genres, API_BASEURL + 'genres')
api.add_resource(Suggestions, API_BASEURL + 'suggestions')
api.add_resource(Films, API_BASEURL + 'films')
api.add_resource(Actor, API_BASEURL + 'actors')
api.add_resource(Directors, API_BASEURL + 'directors')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4242')
