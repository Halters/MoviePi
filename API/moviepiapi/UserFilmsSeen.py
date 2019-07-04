##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# UserFilmsSeen.py
##

from flask_restful import Resource
from flask import request
from moviepiapi.utils import fill_return_packet, userH, check_auth_token
import jwt


class UserFilmsSeen(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def get(self):
        user_uuid = check_auth_token(request)
        user_uuid = "5c1b5841-b8cf-4bbb-ae87-fb6e87b88e21"
        if not user_uuid:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        user_binary = userH.getUUIDBinaryFromStr(user_uuid)
        userInfos = userH.getUserInformations(user_uuid=user_binary)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        filmsSeen = userH.getUserFilmsSeen(userInfos['id'])
        return fill_return_packet(1, "OK", filmsSeen)
