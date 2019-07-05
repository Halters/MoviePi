##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Directors.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request


class Directors(Resource):
    def get(self, director_id):
        result = db.request("SELECT * from director where id=%s", director_id)
        if not result:
            return fill_return_packet(0, "Pas de réalisateur trouvé a l'id demandé", None)
        return result
