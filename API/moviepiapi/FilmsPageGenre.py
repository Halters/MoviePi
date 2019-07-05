##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db, userH, check_auth_token
from flask import request


class FilmsPageGenre(Resource):
    filmsPerPage = 15

    def get(self, page, genre):
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
                "SELECT t1.id, t1.title, t1.release_date, t1.image FROM films AS t1 INNER JOIN films_genres AS t2 WHERE t2.fk_genres = %s AND t1.adult = 0 LIMIT %s, %s", int(genre), start, self.filmsPerPage)
        else:
            result = db.request(
                "SELECT t1.id, t1.title, t1.release_date, t1.image FROM films AS t1 INNER JOIN films_genres AS t2 WHERE t2.fk_genres = %s LIMIT %s, %s", int(genre), start, self.filmsPerPage)
        if not result:
            return fill_return_packet(0, "Pas de film trouvé pour ce genre", None)
        return fill_return_packet(1, "OK", result)
