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
    def get(self, page):
        numberPage = 15
        start = int(page) * numberPage
        result = db.request(
            "SELECT * from films LIMIT %s, %s", start, numberPage)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return result
