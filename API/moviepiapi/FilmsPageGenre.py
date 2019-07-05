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
        if not page or not genre:
            return fill_return_packet(0, "Une page et un genre sont nécessaire", None)
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token Invalide", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Ce compte n'existe pas", None)
        start = int(page) * self.filmsPerPage
        if not start:
            return fill_return_packet(0, "Une erreur est survenue", None)
        if user["age"] < 18:
            result = db.request(
                "SELECT t1.id, t1.title, t1.release_date, t1.image FROM films AS t1 INNER JOIN films_genres AS t2 WHERE t1.adult = 0 AND t2.fk_films = t1.id AND t2.fk_genres LIKE '%%" +
                str(genre) + "%%' LIMIT " + str(start) +
                "," + str(self.filmsPerPage))
        else:
            result = db.request(
                "SELECT t1.id, t1.title, t1.release_date, t1.image FROM films AS t1 INNER JOIN films_genres AS t2 WHERE t2.fk_films = t1.id AND t2.fk_genres LIKE '%%" +
                str(genre) + "%%' LIMIT " + str(start) +
                "," + str(self.filmsPerPage))
        if not result:
            return fill_return_packet(0, "Pas de film trouvé pour ce genre", None)
        return fill_return_packet(1, "OK", result)
