##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Genres.py
##

from flask_restful import Resource
from flask import request
from moviepiapi.utils import fill_return_packet, userH, check_auth_token


class UserGenres(Resource):
    def get(self):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        userInfos = userH.getUserInformations(user_uuid=uuid)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        genres = userH.getUserGenres(userInfos['id'])
        return fill_return_packet(1, "OK", genres)
