##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## User.py
##

from flag import Flag
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from flask_api import status
from utils import *
import json
import hashlib
import jwt
import uuid
import time

class User(Resource):
    data_information = {'userInfos' : None, 'JWT' : ""}

    def post(self):
        packet = request.json
        print(packet)
        username = packet['username']
        password = packet['password']
        password = hashlib.sha256(password.encode('utf_8'))
        password = password.hexdigest()
        user_uuid = uuid.uuid4()
        age = int(packet['age'])
        conn = db_connect.connect()
        query = conn.execute("INSERT INTO users (username, age, password, uuid) VALUES (%s,%s,%s,_binary %s)", username, age, password, user_uuid.bytes)
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "Echec à la création du compte", None)
            return ret_packet
        self.data_information['userInfos'] = result
        token_payload["sub"] = str(user_uuid)
        self.data_information['JWT'] = jwt.encode(token_payload, Key, algorithm='HS256').decode('utf-8')
        ret_packet = fill_return_packet(1, "Création du compte OK.", self.data_information)
        ret_packet['exp'] = int(time.time() + 86400)
        return ret_packet