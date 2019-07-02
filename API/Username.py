##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## Username.py
##

from flask_restful import Resource
from utils import *
from flask import request
import json

class Username(Resource):
    def get(self, username):
        packet = request.args
        print("TEST ======== ", username)
        if (len(username) > LEN_MAX_USER):
            ret_packet = fill_return_packet(0, "La limite de caractère est de 255", False)
            return ret_packet
        conn = db_connect.connect()
        query = conn.execute("SELECT * From users WHERE username=%s", username)
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        print(result)
        if result:
            ret_packet = fill_return_packet(0, "Le nom d'utilisateur est déjà utilisé", False)
            return ret_packet
        if not result:
            ret_packet = fill_return_packet(1, "Le nom d'utilisateur est valide", True)
            return ret_packet