##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## usersPreferences.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, Key, userH, encode_auth_token, check_auth_token, ret_packet, db, make_average_weight
from flask import request

class usersPreferences(Resource):
    data_informations = {'userInfos' : None, "JWT" : ""}

    def update(self):
    uuid = check_auth_token(request)
    if not uuid:
        return fill_return_packet(0, "Token Invalide", None)
    uuid_binary = userH.getUUIDBinaryFromStr(uuid)
    user = userH.getUserInformations(user_uuid=uuid_binary)
    if not user:
        return fill_return_packet(0, "Ce compte n'existe pas", self.data_informations)
    print (request)
    print (user)