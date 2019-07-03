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
    data_information = {'userInfos': None, 'JWT': ""}

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
        print(newUser)
        userH.setUserGenres(newUser['id'], packet['genres'])
        newUser['genres'] = userH.getUserGenres(newUser['id'])
        self.data_information['userInfos'] = newUser
        token_payload["sub"] = str(newUser['uuid'])
        self.data_information['JWT'] = jwt.encode(
            token_payload, Key, algorithm='HS256').decode('utf-8')
        ret_packet = fill_return_packet(
            1, "Création du compte OK.", self.data_information)
        ret_packet['exp'] = int(time.time() + 86400)
        return ret_packet
