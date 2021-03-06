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

###############################################################################
#                               IMPORT ROUTE                                  #
###############################################################################
from moviepiapi.ActorDetails import ActorDetails
from moviepiapi.CastingList import CastingList
from moviepiapi.CrewDetails import CrewDetails
from moviepiapi.CrewList import CrewList
from moviepiapi.Films import Films
from moviepiapi.FilmsPage import FilmsPage
from moviepiapi.FilmsPageGenre import FilmsPageGenre
from moviepiapi.Genres import Genres
from moviepiapi.Suggestions import Suggestions
from moviepiapi.User import User
from moviepiapi.UserComments import UserComments
from moviepiapi.UserFilmsSeen import UserFilmsSeen
from moviepiapi.UserGenres import UserGenres
from moviepiapi.Username import Username
from moviepiapi.Users import Users
from moviepiapi.usersPreferences import usersPreferences
from moviepiapi.UserNote import UserNote
from moviepiapi.ActivityThread import ActivityThread

###############################################################################
#                               IMPORT SYSTEM                                 #
###############################################################################
from flask_cors import CORS
from flask_restful import Resource, Api
from flask import Flask, request, jsonify


app = Flask(__name__)
api = Api(app)
CORS(app)

API_SUBURL = '/api'
API_VERSION = '1'

API_BASEURL = API_SUBURL + '/v' + API_VERSION + '/'


###############################################################################
#                               ROUTE                                         #
###############################################################################
api.add_resource(ActivityThread, API_BASEURL + 'activitythread')
api.add_resource(ActorDetails, API_BASEURL + 'actordetails/<actor_id>')
api.add_resource(CastingList, API_BASEURL + 'castinglist/<film_id>')
api.add_resource(CrewDetails, API_BASEURL + 'crewdetails/<crew_id>')
api.add_resource(CrewList, API_BASEURL + 'crewlist/<film_id>')
api.add_resource(Films, API_BASEURL + 'films/<film_id>')
api.add_resource(FilmsPage, API_BASEURL + 'films/page/<page>')
api.add_resource(FilmsPageGenre, API_BASEURL + 'films/page/<page>/<genre>')
api.add_resource(UserGenres, API_BASEURL + 'user/genres')
api.add_resource(Suggestions, API_BASEURL + 'suggestions')
api.add_resource(User, API_BASEURL + 'user')
api.add_resource(UserComments, API_BASEURL + 'users/comment/<film_id>')
api.add_resource(UserFilmsSeen, API_BASEURL + 'user/filmsSeen')
api.add_resource(Username, API_BASEURL + 'checkUsername/<username>')
api.add_resource(UserNote, API_BASEURL + 'usernote/<film_id>',
                 API_BASEURL + 'usernote/<film_id>/<note>')
api.add_resource(Users, API_BASEURL + 'users')
api.add_resource(usersPreferences, API_BASEURL + 'user/settings')
api.add_resource(Genres, API_BASEURL + 'genres')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4242')
