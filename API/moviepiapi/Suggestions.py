##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Suggestions.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, userH, encode_auth_token, check_auth_token, db, make_average_weight
from flask import request
import random

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
        to_select = ""
        list_suggestions = []
        good_suggestions = ""
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
        average = make_average_weight(weight_list)
        for i in range(len(weight_list)):
            if weight_list[i] >= average:
                tag_list.append(id_list[i])
        print(tag_list)
        to_select = "'%%" + str(tag_list[0]) + "%%'"
        cmd = "SELECT fk_films FROM films_genres WHERE fk_genres LIKE " +  to_select
        result = db.request(cmd)
        for i in range(10):
            selected = random.randint(1,len(result))
            list_suggestions.append(result[selected])
        
        for i in range(len(list_suggestions)):
            good_suggestions = good_suggestions + str(list_suggestions[i]['fk_films']) + ","
        good_suggestions = good_suggestions[:-1]
        result = db.request("SELECT * from films WHERE id IN(" + good_suggestions +")")
        if not result:
            return fill_return_packet(0, "Aucune propositions trouvées", None)
        for i in range(len(result)):
            del result[i]['id_tmdb']
        return fill_return_packet(1, "OK", result)
        