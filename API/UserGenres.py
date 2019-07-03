##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Genres.py
##

from flask_restful import Resource
from flask import request
from utils import fill_return_packet, userH


class UserGenres(Resource):
    def get(self, uuid):
        userInfos = userH.getUserInformations(user_uuid=uuid)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        genres = userH.getUserGenres(userInfos['id'])
        return fill_return_packet(0, None, genres)

    def post(self):
        packet = request.json
        # newGenres = packet["genres"]
        # userH.setUserGenres(0, newGenres)
        # return fill_return_packet(0, None, userH.getUserGenres(0))
