##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# utils.py
##

import time
from dbHelper import dbHelper
from userHelper import userHelper

ret_packet = {'responseStatus': 0, 'message': "", 'data': any, "exp": 0}
token_payload = {'sub': "", "exp": (int(time.time()) + 86400)}
Key = 'MoviePiTheoAudreyHicham'
LEN_MAX_USER = 255

db = dbHelper('moviepi_api', 'moviepi_api', 'moviepi', '51.75.141.254')
userH = userHelper(db, LEN_MAX_USER)


def fill_return_packet(iswork, typeoferror, data):
    ret_packet['responseStatus'] = iswork
    ret_packet['message'] = typeoferror
    ret_packet['data'] = data
    return ret_packet
