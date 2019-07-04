##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## Suggestions.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, Key, userH, encode_auth_token, check_auth_token, ret_packet, db, make_average_weight
from flask import request

class Suggestions(Resource):
    data_information = {'userInfos' : None, 'JWT' : ""}

    def get(self):
        user_uuid = check_auth_token(request)
        id_list = []
        weight_list = []
        tag_list = []
        tag_str = []
        list_str = ""
        if not user_uuid:
            return fill_return_packet(0, "Invalid Token", None)
        uuid_binary = userH.getUUIDBinaryFromStr(user_uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Compte inexistant", self.data_information)
        result = db.request("SELECT fk_genres, weight from users_genres WHERE fk_users=%s", user['id'])
        if not result:
            return fill_return_packet(0, "Pas de préférences pour cette utilisateur", self.data_information)
        print(result)
        for i in range(len(result)):
            id_list.append(result[i]['fk_genres'])
            weight_list.append(result[i]['weight'])
        result = make_average_weight(weight_list)
        for i in range(len(weight_list)):
            if weight_list[i] >= result:
                tag_list.append(id_list[i])
        for i in range(len(tag_list)):
            result = db.request("SELECT name from genres WHERE id=%s", tag_list[i])
            tag_str.append(result[0]['name'])
        for i in range (len(tag_str)):
            list_str = list_str +  "LIKE('%%" + tag_str[i] + "%%')" + " and genres "
        list_str = list_str[:-13]
        cmd = "SELECT id, title, image FROM films WHERE genres " + list_str + ')'
        result = db.request(cmd)
        print(result)
