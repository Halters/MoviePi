##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db, userH, check_auth_token
from flask import request


class FilmsPage(Resource):
    def get(self, page):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token Invalide", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Ce compte n'existe pas", None)
        numberPage = 15
        start = int(page) * numberPage
        if user["age"] < 18:
            result = db.request(
                "SELECT id, title, release_date, image from films LIMIT %s, %s WHERE adult = 1", start, numberPage)
        else:
            result = db.request(
                "SELECT id, title, release_date, image from films LIMIT %s, %s", start, numberPage)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return result
