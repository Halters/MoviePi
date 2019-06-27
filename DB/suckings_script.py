#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## MoviePi
## File description:
## suckings_cript.py
##

import sys
import requests
import json
import time

def get_tag_list():
    requ_str = "https://api.themoviedb.org/3/genre/movie/list?api_key=f337b9ba57004f5c9ea2785b623c0439&manguage=en-US"
    requ_obj = requests.get(requ_str)
    tag = requ_obj.json()
    temp = json.dumps(tag)
    list_id = []
    list_tag = []
    #for i in range(len(temp)):
    #    print(temp[i])
    print(temp.split(','))
    #print (list_tag[0])


def main(argv):
    #id_max = requests.get("https://api.themoviedb.org/3/movie/%d?api_key=f337b9ba57004f5c9ea2785b623c0439")
    #id_movie = argv[1] 
    #test = r.json()
    tag_list = get_tag_list()
    #print(test["genres"])
    #while(id):
    #    r_tmdb = "https://api.themoviedb.org/3/movie/" + id_movie + "api_key=f337b9ba57004f5c9ea2785b623c0439"
    #    req_exec = requests.get(r_tmdb)
    #    formating = req_exec.json()
    #    id_movie += 1

main(sys.argv)