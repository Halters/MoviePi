##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Suggestions.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, userH, encode_auth_token, check_auth_token, db, make_average_weight
from flask import request

###############################################################################
#                               SUGGESTIONS                                   #
#                    DOC : DOCUMENTATIONS/SUGGESTIONS.MD                      #
###############################################################################


class Suggestions(Resource):
    data_information = {'userInfos': None, 'JWT': ""}

    def get(self):
        user_uuid = check_auth_token(request)
        id_list = []
        weight_list = []
        tag_list = []
        temp_list = []
        list_str = ""
        if not user_uuid:
            return fill_return_packet(0, "Invalid Token", None)
        uuid_binary = userH.getUUIDBinaryFromStr(user_uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Compte inexistant", self.data_information)
        result = db.request(
            "SELECT fk_genres, weight from users_genres WHERE fk_users=%s", user['id'])
        if not result:
            return fill_return_packet(0, "Pas de préférences pour cette utilisateur", self.data_information)
        for i in range(len(result)):
            id_list.append(result[i]['fk_genres'])
            weight_list.append(result[i]['weight'])
        result = make_average_weight(weight_list)
        for i in range(len(weight_list)):
            if weight_list[i] >= result:
                tag_list.append(id_list[i])
        for i in range(len(tag_list)):
            list_str = list_str + \
                "LIKE('%%" + str(id_list[i]) + "%%')" + " and fk_genres "
        list_str = list_str[:-14]
        cmd = "SELECT fk_films FROM films_genres WHERE fk_genres " + list_str
        result = db.request(cmd)
        for i in range(len(result)):
            temp_list.append(result[i]['fk_films'])
        list_str = ""
        print(temp_list)
        for i in range(20) or len(temp_list):
            list_str = list_str + str(temp_list[i]) + ","
        list_str = list_str[:-7]
        cmd = "SELECT * FROM films WHERE id IN(" + list_str + ")"
        result = db.request(cmd)
        for i in range(len(result)):
            del result[i]['id_tmdb']
        isAdult = db.request("SELECT age FROM users WHERE id=%s", user['age'])
        if not isAdult:
            return fill_return_packet(0, "Ce compte n'a pas d'age", None)
        for i in range(len(result)):
            if (result[i]['adult'] == 1 and int(isAdult[0]['age']) < 18):
                del result[i]
        return fill_return_packet(1, "OK", result)
