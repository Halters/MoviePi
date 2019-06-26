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
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
movie_connect = create_engine('mysql+pymysql://root:Sphinxdepau40@@localhost:3306/TMDB')
user_connect = create_engine('mysql+pymysql://root:Sphinxdepau40@@localhost:3306/ACCOUNT_BASE')
api = Api(app)


class Account(Resource):
    def post(self, info_account):
        av = request.args
        tosearch = info_account.split(',')
        conn = user_connect.connect()
        query = conn.execute("INSERT INTO account_info (username, emailaddress, password) VALUES (%s,%s,%s)", tosearch[0], tosearch[1], tosearch[2])
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)

class Tag(Resource):
    def get(self):
        #av = request.args
        #try :
        #    nb_to_return = int(nbtag)
        #except ValueError:
        #    nb_to_return = 0
        cmd = "SELECT genres FROM mytable GROUP BY genres"
        conn = movie_connect.connect()
        query = conn.execute(cmd)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        for genre, tags in result.items():  
            print(genre, ",", tags)
        #for i in query.cursor:
        #    print(i)
        conn.close()
        #return jsonify(result)

class Suggestion(Resource):
    def get(self, flag_str, already_seen):
        args = request.args
        print(flag_str)
        flag = flag_str.split(',')
        flag_list = []
        bestlist = []
        list_str = ""
        value = 0.0
        for x in range (len(flag)):
            temp = Flag(flag[x])
            flag_list.append(temp)
        for x in range (len(flag_list)):
            value = value + flag_list[x].flag_weight
        value = value / len(flag_list)
        for x in range (len(flag_list)):
            if (flag_list[x].flag_weight >= value):
                bestlist.append(flag_list[x].flag_name)
        qsdqsddsq = "%".join(bestlist)
        cmd = "SELECT original_title,director,genres FROM mytable WHERE genres "
        for i in range (len(bestlist)):
            list_str = list_str +  "LIKE('%%" + bestlist[i] + "%%')" + " and genres "
        list_str = list_str[:-13]
        cmd = cmd + list_str + ')'
        print("CMD ======= ", cmd)
        print("SELECT original_title,director,genres FROM mytable WHERE genres LIKE('%%action%%') AND genres LIKE('%%adventure%%')")
        conn = movie_connect.connect()
        query = conn.execute(cmd)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)


class Search(Resource):
    def get(self, command):
        args = request.args #retrieve args from query string
        tosearch = command.split('=')
        conn = movie_connect.connect() # connect to database
        if (tosearch[0] == 'director'):
            query = conn.execute("SELECT original_title,director,genres FROM mytable WHERE director LIKE '%%{}%%'".format(tosearch[1]))
        if (tosearch[0] == 'title'):
            query = conn.execute("SELECT original_title,genres FROM mytable WHERE original_title LIKE '%%{}%%'".format(tosearch[1]))
        if (tosearch[0] == 'cast'):
            query = conn.execute("SELECT original_title,cast FROM mytable WHERE cast LIKE '%%{}%%'".format(tosearch[1]))
        if (tosearch[0] == 'genres'):
            query = conn.execute("SELECT genres,original_title FROM mytable WHERE genres LIKE '%%{}%%'".format(tosearch[1]))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)

api.add_resource(Search,'/filmsearch/<command>') # Route_1
api.add_resource(Account,'/account/<info_account>') # Route 2
api.add_resource(Suggestion,'/sugg/<flag_str> <already_seen>')
api.add_resource(Tag,'/tag')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')