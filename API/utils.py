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
    for i in range (len(list)):
        result = result + float(list[i])
    result = result / len(list)
    print(result)
    return(result)