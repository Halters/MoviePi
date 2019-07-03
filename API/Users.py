##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Users.py
##

from flask_restful import Resource
from utils import fill_return_packet, db, Key, ret_packet, LEN_MAX_USER, token_payload, userH
from flask import request
import hashlib
import jwt
import time
import uuid


class Users(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def get(self):
        packet = request.json
        uuid_find = str(packet[0]['uuid'])
        result = db.request("SELECT * FROM users WHERE uuid=%s", uuid_find)
        if not result:
            ret_packet = fill_return_packet(0, "User not found", None)
            return ret_packet
        self.data_information['userInfos'] = result[0]
        self.data_information[0]['JWT'] = result[0]['JWT']
        ret_packet = fill_return_packet(1, "OK", self.data_information)
        return ret_packet

    def post(self):
        packet = request.json
        username = str(packet["username"])
        password = str(packet["password"])
        user = userH.getUserForAuth(username, password)
        if not user:
            return fill_return_packet(
                0, "Account doesn't exist", self.data_information)
        user['genres'] = userH.getUserGenres(user['id'])
        user['uuid'] = userH.getUUIDstrFromBinary(user['uuid'])
        del user['id']
        self.data_information['userInfos'] = user
        token_payload["sub"] = user['uuid']
        self.data_information['exp'] = (int(time.time()) + 86400)
        self.data_information['JWT'] = jwt.encode(
            token_payload, Key, algorithm='HS256').decode('utf-8')
        ret_packet = fill_return_packet(1, "OK", self.data_information)
        return ret_packet
