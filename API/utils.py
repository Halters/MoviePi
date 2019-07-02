##
## EPITECH PROJECT, 2019
## MoviePi
## File description:
## utils.py
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
token_payload = {'sub' : "", "exp" : (int(time.time()) + 86400)}
Key = 'MoviePiTheoAudreyHicham'
LEN_MAX_USER = 255


db_connect = create_engine('mysql+pymysql://moviepi_api:moviepi_api@51.75.141.254:3306/moviepi')

def fill_return_packet(iswork, typeoferror, data):
        ret_packet['responseStatus'] = iswork
        ret_packet['message'] = typeoferror
        ret_packet ['data'] = data
        return ret_packet