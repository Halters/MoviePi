##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request


class Films(Resource):
    def get(self, film_id):
        result = db.request("SELECT * from films where id=%s", film_id)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return fill_return_packet(1, "OK", result)
