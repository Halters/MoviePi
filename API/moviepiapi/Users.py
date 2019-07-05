##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Users.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, userH, encode_auth_token, check_auth_token
from flask import request


class Users(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def get(self):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Invalid Token", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(
                0, "Ce compte n'existe pas", self.data_information)
        user['genres'] = userH.getUserGenres(user['id'])
        user['uuid'] = uuid
        del user['id']
        self.data_information['userInfos'] = user
        self.data_information['JWT'] = encode_auth_token(uuid)
        return fill_return_packet(1, "OK", self.data_information)

    def post(self):
        packet = request.json
        username = str(packet["username"])
        password = str(packet["password"])
        user = userH.getUserForAuth(username, password)
        if not user:
            return fill_return_packet(
                0, "Ce compte n'existe pas", self.data_information)
        user['genres'] = userH.getUserGenres(user['id'])
        user['uuid'] = userH.getUUIDstrFromBinary(user['uuid'])
        del user['id']
        self.data_information['userInfos'] = user
        self.data_information['JWT'] = encode_auth_token(user['uuid'])
        return fill_return_packet(1, "OK", self.data_information)
