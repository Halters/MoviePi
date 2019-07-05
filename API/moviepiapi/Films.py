##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db, userH, check_auth_token
from flask import request

###############################################################################
#                               FILMS                                         #
#                    DOC : DOCUMENTATION/FILMS.MD                             #
###############################################################################


class Films(Resource):
    def get(self, film_id):
        if not film_id:
            return fill_return_packet(0, "Un ID de film est nécessaire", None)
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token Invalide", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Ce compte n'existe pas", None)
        result = db.request("SELECT * from films where id=%s", film_id)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        if result[0]["adult"] and user["age"] < 18:
            return fill_return_packet(0, "Film adulte", None)
        return fill_return_packet(1, "OK", result)
