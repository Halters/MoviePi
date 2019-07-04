##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## CrewDetails.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request

class CrewDetails(Resource):
    def get(self, crew_id):
        if not crew_id:
            return fill_return_packet(0, "KO", None)
        cmd = "SELECT * from directors WHERE id=" + crew_id
        result = db.request(cmd)
        if not result:
            return fill_return_packet(0, "Le réalisateur n'existe pas", None)
        del result[0]['id_tmdb']
        return fill_return_packet(1, "OK", result)