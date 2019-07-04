##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Actor.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request


class Actor(Resource):

    def get(self, actor_id):
        result = db.request("SELECT * from actors where id=%s", actor_id)
        if not result:
            return fill_return_packet(0, "Pas d'acteur trouvé a l'id demandé", None)
        return result
