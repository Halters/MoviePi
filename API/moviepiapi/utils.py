##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# utils.py
##

import datetime
import jwt
from moviepiapi.dbHelper import dbHelper
from moviepiapi.userHelper import userHelper

ret_packet = {'responseStatus': 0, 'message': "", 'data': any}
Key = 'MoviePiTheoAudreyHicham'
LEN_MAX_USER = 255

db = dbHelper('moviepi_api', 'moviepi_api', 'moviepi', '51.75.141.254')
userH = userHelper(db, LEN_MAX_USER)


def fill_return_packet(iswork, typeoferror, data):
    ret_packet['responseStatus'] = iswork
    ret_packet['message'] = typeoferror
    ret_packet['data'] = data
    return ret_packet


def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            Key,
            algorithm='HS256'
        ).decode('utf-8')
    except Exception as e:
        return e


def check_auth_token(request):
    auth_headers = request.headers.get('Authorization', '').split()
    if len(auth_headers) != 2:
        return None
    try:
        payload = jwt.decode(auth_headers[1], Key)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    return False


def make_average_weight(list):
    result = 0.0
    if not list:
        return -1
    for i in range(len(list)):
        result = result + float(list[i])
    result = result / len(list)
    print(result)
    return(result)

def adjust_weight_user(film_id, note, id_user):
    weight_list = []
    idgenre_list = []
    already_genre = []
    all_genre_user = []
    new_weight = []
    result = db.request("SELECT fk_genres FROM films_genres WHERE id=%s", str(film_id))
    print(result)
    if not result:
        return fill_return_packet(0, "Pas genres trouvés pour ce film", None)
    for i in range(len(result)):
        idgenre_list.append(result[i]['fk_genres'])
    result_user = db.request("SELECT fk_genres, weight FROM users_genres WHERE id=%s", str(id_user))
    print(result_user)
    if not result_user:
        return False
    for i in range(len(result_user)):
        already_genre.append(result_user[i]['fk_genres'])
    final_list = list(set(idgenre_list).union(set(already_genre)))
    for i in range(len(final_list)):
        for y in range(len(result)):
            if final_list[i] == result_user[y]['fk_genres']:
                new_weight.append((int(result_user[i]['weight']) / len(final_list)) * int(note))
            else:
                new_weight.append(1)
    print(new_weight)
    return True

