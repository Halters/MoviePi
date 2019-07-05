##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## CrewList.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db
from flask import request

class CrewList(Resource):
    
    def get(self, film_id):
        temp_str = ""
        list_str = ""
        int_value = []
        if not film_id:
            return fill_return_packet(0, "Aucune ID n'es detecté", None)
        result = db.request("SELECT fk_directors FROM films_directors WHERE fk_films=%s", str(film_id))
        if not result:
            return fill_return_packet(0, "Le film n'a pas de directeur", None)
        temp_str = result[0]['fk_directors'].split(',')
        for i in range(len(temp_str)):
            list_str = list_str + str(temp_str[i]) + ","
        list_str = list_str[:-1]
        cmd = "SELECT id, name, image FROM directors WHERE id IN(" + list_str + ")"
        result = db.request(cmd)
        if not result:
            return fill_return_packet(0, "KO", None)
        return fill_return_packet(1, "OK", result)