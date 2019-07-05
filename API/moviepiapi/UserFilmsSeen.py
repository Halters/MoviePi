##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# UserFilmsSeen.py
##

from flask_restful import Resource
from flask import request
from moviepiapi.utils import fill_return_packet, userH, check_auth_token, db
import jwt


class UserFilmsSeen(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def get(self):
        user_uuid = check_auth_token(request)
        if not user_uuid:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        user_binary = userH.getUUIDBinaryFromStr(user_uuid)
        userInfos = userH.getUserInformations(user_uuid=user_binary)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        filmsSeen = userH.getUserFilmsSeen(userInfos['id'])
        return fill_return_packet(1, "OK", filmsSeen)

    def post(self):
        packet = request.json
        user_uuid = check_auth_token(request)
        if not user_uuid:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        user_binary = userH.getUUIDBinaryFromStr(user_uuid)
        userInfos = userH.getUserInformations(user_uuid=user_binary)
        if not userInfos:
            return fill_return_packet(0, "Pas de données sur cette utilisateur", None)
        result = db.insert("INSERT INTO users_films (fk_users, fk_films) VALUES (%s, %s)", userInfos['id'], packet['id'])
        if not result:
            return fill_return_packet(0, "KO", None)
        return fill_return_packet(1, "OK", None)
        
