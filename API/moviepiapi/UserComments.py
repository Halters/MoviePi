##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# Films.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db, check_auth_token, userH
from flask import request


class UserComments(Resource):
    def get(self, film_id):
        result = db.request(
            "SELECT * FROM comments WHERE fk_films = %s", film_id)
        if not result:
            return fill_return_packet(0, "Aucun commentaire sur ce film", None)
        for comment in result:
            userInfos = db.request(
                "SELECT username FROM users WHERE id = %s", comment["fk_users"])
            if not userInfos:
                pass
            else:
                comment["username"] = userInfos['username']
        return fill_return_packet(1, "OK", result)

    def post(self, film_id):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token invalide", None)
        packet = request.json
        if not packet["comment"]:
            return fill_return_packet(0, "Ce commentaire n'est pas bon", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        userInfos = userH.getUserInformations(user_uuid=uuid_binary)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        result = db.insert(
            "INSERT INTO comments (fk_users, fk_films, comment) VALUES (%s, %s, %s)", userInfos["id"], film_id, packet["comment"])
        if not result:
            return fill_return_packet(0, "Une erreur est survenue", None)
        result = db.request(
            "SELECT * FROM comments WHERE fk_films = %s", film_id)
        for comment in result:
            userInfos = db.request(
                "SELECT username FROM users WHERE id = %s", comment["fk_users"])
            if not userInfos:
                pass
            else:
                comment["username"] = userInfos['username']
        return fill_return_packet(1, "OK", result)

    def patch(self, film_id):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token invalide", None)
        packet = request.json
        if not packet["comment"] or packet["id_comment"]:
            return fill_return_packet(0, "Ce commentaire n'est pas bon", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        userInfos = userH.getUserInformations(user_uuid=uuid_binary)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        original_comment = db.request(
            "SELECT * FROM comments WHERE id = %s AND fk_users = %s AND fk_films = %s", packet["id_comment"], userInfos["id"], film_id)
        if not original_comment:
            return fill_return_packet(0, "Ce commentaire n'existe pas", None)
        db.request(
            "UPDATE comments SET comment = %s WHERE id = %s", packet["comment"], packet["id_comment"])
        result = db.request(
            "SELECT * FROM comments WHERE fk_films = %s", film_id)
        for comment in result:
            userInfos = db.request(
                "SELECT username FROM users WHERE id = %s", comment["fk_users"])
            if not userInfos:
                pass
            else:
                comment["username"] = userInfos['username']
        return fill_return_packet(1, "OK", result)

    def delete(self, film_id):
        uuid = check_auth_token(request)
        if not uuid:
            return fill_return_packet(0, "Token invalide", None)
        if not film_id:
            return fill_return_packet(0, "Ce commentaire n'existe pas", None)
        uuid_binary = userH.getUUIDBinaryFromStr(uuid)
        userInfos = userH.getUserInformations(user_uuid=uuid_binary)
        if not userInfos:
            return fill_return_packet(0, "Cet utilisateur n'existe pas", None)
        db.request(
            "DELETE FROM comments WHERE id = %s AND fk_users = %s", film_id, userInfos["id"])
        result = db.request(
            "SELECT * FROM comments WHERE fk_films = %s", film_id)
        for comment in result:
            userInfos = db.request(
                "SELECT username FROM users WHERE id = %s", comment["fk_users"])
            if not userInfos:
                pass
            else:
                comment["username"] = userInfos['username']
        return fill_return_packet(1, "OK", result)
