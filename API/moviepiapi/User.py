##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# User.py
##

from flask import request
from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, Key, userH, encode_auth_token


class User(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def post(self):
        packet = request.json
        username = packet['userInfos']['username']
        password = packet['userInfos']['password']
        age = int(packet['userInfos']['age'])
        newUser = userH.createNewUser(username, password, age)
        if not newUser:
            return fill_return_packet(
                0, "Echec à la création du compte", None)
        userH.setUserGenres(newUser['id'], packet['genres'])
        newUser['genres'] = userH.getUserGenres(newUser['id'])
        del newUser['id']
        newUser['uuid'] = userH.getUUIDstrFromBinary(newUser['uuid'])
        self.data_information['userInfos'] = newUser
        self.data_information['JWT'] = encode_auth_token(newUser['uuid'])
        return fill_return_packet(
            1, "Création du compte OK.", self.data_information)
