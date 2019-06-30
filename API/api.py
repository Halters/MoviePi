#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## api_gateway
## File description:
## api.py
##

from flag import Flag
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from flask_api import status
import json
import hashlib
import jwt
import uuid
import time

ret_packet = {'responseStatus' : 0, 'message' : "", 'data' : any, "exp" : 0}
token_header ={'alg' : "HS256", "typ" : "JWT"}
token_payload = {'sub' : 0, "exp" : (int(time.time()) + 86400)}
Key = 'MoviePiTheoAudreyHicham'

db_connect = create_engine('mysql+pymysql://moviepi_api:moviepi_api@51.75.141.254:3306/moviepi')

app = Flask(__name__)
api = Api(app)
CORS(app)

def fill_return_packet(iswork, typeoferror, data):
        ret_packet['responseStatus'] = iswork
        ret_packet['message'] = typeoferror
        ret_packet ['data'] = data
        return ret_packet

def create_new_token(packet):
    ret_packet['responseStatus'] = 1
    ret_packet['message'] = "New Token generate"
    ret_packet[0]['data'] = packet[0]
    ret_packet[1]['data'] = 

class User(Resource):
    def post(self):
        packet = request.json

    ##def get(self, command):

    ##def update(self, command):


class Users(Resource):
    data_information = {'userInfos' : None, 'JWT' : ""}

    def get(self):
        packet = request.json
        

    def post(self):
        packet = request.json
        username = str(packet["username"])
        pwd = str(packet["password"])
        hash_pwd = hashlib.sha256(pwd.encode('utf_8'))
        hex_dig = hash_pwd.hexdigest()
        if packet[0]['JWT']:
            checker = packet[0]['exp']
            if checker >= int(time.time()) + 86400:
                ret_packet = fill_return_packet(0, "Token expired", None)
            conn = db_connect.connect()
            query = conn.execute("SELECT * FROM users WHERE uuid=%s", packet[0]['uuid'])
            result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
            if not result:
                ret_packet = fill_return_packet(0, "No uuid find in the db", None)
                return ret_packet
            self.data_information['userInfos'] = result
            self
            return ret_packet
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users WHERE username=%s AND password=%s", username, pwd)
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if not result:
            ret_packet = fill_return_packet(0, "Account doesn't exist", self.data_information)
            return ret_packet
        result[0]['uuid'] = str(uuid.UUID(bytes=result[0]['uuid']))
        self.data_information['userInfos'] = result[0]
        token_payload['sub'] = result[0]['uuid']
        self.data_information[0]['JWT'] = token_header
        self.data_information[1]['JWT'] = token_payload
        self.data_information[2]['JWT'] =  jwt.encode(token_payload, Key, algorithm='HS256').decode('utf-8')
        ret_packet = fill_return_packet(1, "OK", self.data_information)
        return ret_packet


api.add_resource(Users, '/api/v1/users') # Route_1 // TYPE = POST
##api.add_resource(User, '/user/register/') # Route 2 // TYPE = POST
#api.add_resource(User, '/user/<id>') # Route 3 // TYPE = GET
#api.add_resource(User, '/user/<id>') # Route 4 // TYPE = UPDATE
if __name__ == '__main__':
     app.run(host='0.0.0.0', port='4242')