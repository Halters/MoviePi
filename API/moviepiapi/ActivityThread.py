##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# ActivityThread.py
##

from flask_restful import Resource
from flask import request
from moviepiapi.utils import fill_return_packet, db


class ActivityThread(Resource):
    def get(self):
        result = db.request("SELECT COUNT(*) FROM films")
        if not result:
            return fill_return_packet(0, "KO", None)
        to_return = int(result[0]['COUNT(*)'] / 15)
        return fill_return_packet(1, "OK", to_return)
