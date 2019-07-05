##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# usersPreferences.py
##

from flask_restful import Resource
from moviepiapi.utils import check_auth_token, userH, fill_return_packet, encode_auth_token
from flask import request


class usersPreferences(Resource):
    data_informations = {'userInfos': None, "JWT": ""}

    def update(self):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token Invalide", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Ce compte n'existe pas", None)
        packet = request.json
        username = packet["username"] if packet["username"] else user["username"]
        password = userH.hashPassword(
            packet["password"]) if packet["password"] else None
        age = packet["age"] if packet["age"] else user["age"]
        user = userH.updateUserInfos(user["id"], username, password, age)
        if not user:
            return fill_return_packet(0, "Une erreur est survenue", None)
        self.data_informations["JWT"] = encode_auth_token(user["uuid"])
        del user["id"]
        self.data_informations["userInfos"] = user
        return fill_return_packet(1, None, self.data_informations)
