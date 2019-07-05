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
    filmsPerPage = 15

    def get(self, page):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token Invalide", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Ce compte n'existe pas", None)
        start = int(page) * self.filmsPerPage
        if user["age"] < 18:
            result = db.request(
                "SELECT id, title, release_date, image from films LIMIT %s, %s WHERE adult = 0", start, self.filmsPerPage)
        else:
            result = db.request(
                "SELECT id, title, release_date, image from films LIMIT %s, %s", start, self.filmsPerPage)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé a l'id demandé", None)
        return fill_return_packet(1, "OK", result)
