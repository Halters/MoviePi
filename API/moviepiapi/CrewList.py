##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# CrewList.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request

###############################################################################
#                               CREW LIST                                     #
#                    DOC : DOCUMENTATION/CREWLIST.MD                          #
###############################################################################


class CrewList(Resource):
    def get(self, film_id):
        if not film_id:
            return fill_return_packet(0, "Aucune ID n'es detecté", None)
        result = db.request(
            "SELECT fk_directors FROM films_directors WHERE fk_films=%s", str(film_id))
        if not result:
            return fill_return_packet(0, "Le film n'a pas de réalisateur", None)
        crew_list = result[0]['fk_directors']
        query = "SELECT id, name, image FROM directors WHERE id IN(" + \
            crew_list + ")"
        result = db.request(query)
        if not result:
            return fill_return_packet(0, "KO", None)
        return fill_return_packet(1, "OK", result)
