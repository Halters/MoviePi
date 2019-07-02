##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Genres.py
##

from flask_restful import Resource
from utils import db_connect, fill_return_packet


class Genres(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * from genres")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "No genres are found", None)
            return ret_packet
        ret_packet = fill_return_packet(1, "OK", result)
        return ret_packet
