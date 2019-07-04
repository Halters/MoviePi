##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, Key, userH, encode_auth_token, check_auth_token, ret_packet, db, make_average_weight
from flask import request

class Films(Resource):
    def get(self, film_id):
        result = db.request("SELECT * from films where id=%s", film_id)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return result