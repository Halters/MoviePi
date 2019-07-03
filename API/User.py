##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# User.py
##

from flask import request
from flask_restful import Resource
from utils import db, fill_return_packet, token_payload, Key, userH
import jwt
import time


class User(Resource):
    data_information = {'userInfos': None, 'JWT': "", 'exp': 0}

    def post(self):
        packet = request.json
        username = packet['username']
        password = packet['password']
        age = int(packet['age'])
        newUser = userH.createNewUser(username, password, age)
        if not newUser:
            ret_packet = fill_return_packet(
                0, "Echec à la création du compte", None)
            return ret_packet
        userH.setUserGenres(newUser['id'], packet['genres'])
        newUser['genres'] = userH.getUserGenres(newUser['id'])
        del newUser['id']
        newUser['uuid'] = userH.getUUIDstrFromBinary(newUser['uuid'])
        self.data_information['userInfos'] = newUser
        token_payload["sub"] = str(newUser['uuid'])
        self.data_information['JWT'] = jwt.encode(
            token_payload, Key, algorithm='HS256').decode('utf-8')
        self.data_information['exp'] = int(time.time() + 86400)
        result = fill_return_packet(
            1, "Création du compte OK.", self.data_information)
        return result
