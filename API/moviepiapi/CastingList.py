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
        if not film_id:
            return fill_return_packet(0, "Aucune ID n'est detecté", None)
        result = db.request(
            "SELECT fk_actors FROM films_casting WHERE fk_films=%s", str(film_id))
        if not result:
            return fill_return_packet(0, "Le film n'a aucun casting", None)
        casting_list = result[0]['fk_actors']
        query = "SELECT id, name, image FROM actors WHERE id IN(" + \
            casting_list + ")"
        result = db.request(query)
        if not result:
            return fill_return_packet(0, "KO", None)
        return fill_return_packet(1, "OK", result)
