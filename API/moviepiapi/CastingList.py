##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# actorList.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request

###############################################################################
#                               CASTING LIST                                  #
#                    DOC : DOCUMENTATION/CASTINGLIST.MD                       #
###############################################################################


class CastingList(Resource):
    def get(self, film_id):
        temp_str = ""
        list_str = ""
        if not film_id:
            return fill_return_packet(0, "Aucune ID n'es detecté", None)
        result = db.request(
            "SELECT fk_actors FROM films_casting WHERE fk_films=%s", str(film_id))
        if not result:
            return fill_return_packet(0, "Le film n'a aucun casting", None)
        temp_str = result[0]['fk_actors'].split(',')
        for i in range(len(temp_str)):
            list_str = list_str + str(temp_str[i]) + ","
        list_str = list_str[:-1]
        cmd = "SELECT id, name, image FROM actors WHERE id IN(" + \
            list_str + ")"
        result = db.request(cmd)
        if not result:
            return fill_return_packet(0, "KO", None)
        return fill_return_packet(1, "OK", result)
