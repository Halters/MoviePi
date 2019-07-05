##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# UserNote.py
##

from flask_restful import Resource
from moviepiapi.utils import fill_return_packet, db, check_auth_token, userH, adjust_weight_user
from flask import request

###############################################################################
#                               USER NOTE                                     #
#                    DOC : DOCUMENTATION/USERNOTE.MD                          #
###############################################################################


class UserNote(Resource):
    def patch(self, film_id, note):
        user_uuid = check_auth_token(request)
        if not film_id or not note:
            return fill_return_packet(0, "Un des parametres est manquant ou invalide", None)
        if not user_uuid:
            return fill_return_packet(0, "Invalid Token", None)
        uuid_binary = userH.getUUIDBinaryFromStr(user_uuid)
        user = userH.getUserInformations(user_uuid=uuid_binary)
        if not user:
            return fill_return_packet(0, "Compte inexistant", None)
        db.insert("INSERT INTO users_ratings (fk_users, fk_films, rating) VALUES (%s, %s, %s)",
                  user['id'], film_id, note)
        checker = db.request(
            "SELECT * FROM users_ratings WHERE fk_users=%s AND fk_films=%s", user['id'], film_id)
        if not checker:
            return fill_return_packet(0, "L'ajout des données a la DB a échoué", None)
        if (adjust_weight_user(film_id, note, int(user['id'])) == False):
            return fill_return_packet(0, "L'ajustement des poids a échoué", None)
        return fill_return_packet(1, "OK", None)
