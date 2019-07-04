##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## ActorDetails.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request

class ActorDetails(Resource):
    def get(self, actor_id):
        if not actor_id:
            return fill_return_packet(0, "KO", None)
        cmd = "SELECT * from actors WHERE id=" + actor_id
        result = db.request(cmd)
        if not result:
            return fill_return_packet(0, "L'acteur n'existe pas", None)
        del result[0]['id_tmdb']
        return fill_return_packet(1, "OK", result)