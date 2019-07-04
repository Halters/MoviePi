##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request


class FilmsPage(Resource):
    def get(self, film_id):
        result = None
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return result
