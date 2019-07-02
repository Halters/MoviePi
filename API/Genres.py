##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## Genres.py
##

from utils import *




class Genres(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * from genres")
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "No genres are found", None)
            return ret_packet
        ret_packet = fill_return_packet(1, "OK", result);
        return ret_packet