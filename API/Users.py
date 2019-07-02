##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## Users.py
##

from flask_restful import Resource
from utils import fill_return_packet, db_connect, Key, ret_packet, LEN_MAX_USER,token_payload
from flask import request
import hashlib
import json
import jwt
import time
import uuid

class Users(Resource):
    data_information = {'userInfos' : None, 'JWT' : ""}

    def get(self):
        packet = request.json
        uuid_find = str(packet[0]['uuid'])
        conn = db_connect.connect()
        query= conn.execute("SELECT * FROM users WHERE uuid=%s", uuid_find)
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "User not found", None)
            return ret_packet
        self.data_information['userInfos'] = result[0]
        self.data_information[0]['JWT'] = result[0]['JWT']
        ret_packet = fill_return_packet(1, "OK", self.data_information)
        return ret_packet

    def post(self):
        packet = request.json
        username = str(packet["username"])
        pwd = str(packet["password"])
        hash_pwd = hashlib.sha256(pwd.encode('utf_8'))
        hex_dig = hash_pwd.hexdigest()
        #if packet[0]['JWT']:
        #    checker = packet['exp']
        #    if checker >= int(time.time()) + 86400:
        #        ret_packet = fill_return_packet(0, "Token expired", None)
        #    conn = db_connect.connect()
        #    query = conn.execute("SELECT * FROM users WHERE uuid=%s", packet[0]['uuid'])
        #    result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        #    if not result:
        #        ret_packet = fill_return_packet(0, "No uuid find in the db", None)
        #        return ret_packet
        #    self.data_information['userInfos'] = result
        #    token_payload['uuid'] = packet[0]['uuid']
        #    token_payload['exp'] = (int(time.time()) + 86400)
        #    ret_packet['exp'] = token_payload['exp']
        #    self.data_information[2]['JWT'] = jwt.encode(token_payload, Key, algorithm='HS256').decode('utf-8')
        #    ret_packet = fill_return_packet()
        #    return ret_packet
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users WHERE username=%s AND password=%s", username, pwd)
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "Account doesn't exist", self.data_information)
            return ret_packet
        self.data_information['userInfos'] = result
        result[0]['uuid'] =  str(uuid.UUID(bytes=result[0]['uuid']))
        token_payload["sub"] = result[0]['uuid']
        self.data_information['JWT'] = jwt.encode(token_payload, Key, algorithm='HS256').decode('utf-8')
        ret_packet = fill_return_packet(1, "OK", self.data_information)
        ret_packet['exp'] = (int(time.time()) + 86400)
        return ret_packet