##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Genres.py
##

from flask_restful import Resource
from utils import db, fill_return_packet


class Genres(Resource):
    def get(self):
        result = db.request("SELECT id, name from genres")
        if not result:
            ret_packet = fill_return_packet(0, "Aucun genre trouvé", None)
            return ret_packet
        ret_packet = fill_return_packet(1, "OK", result)
        return ret_packet
