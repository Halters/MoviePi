##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Username.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, userH
from flask import request


class Username(Resource):
    def get(self, username):
        isValid, message = userH.checkUsername(username)
        return fill_return_packet(1, message, isValid)
