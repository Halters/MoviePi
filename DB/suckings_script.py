#!/usr/bin/env python3

import sys
import requests
import json
import time
from sqlalchemy import create_engine


def add_one_person(requ_str, api_key, conn, id):
    resp = requests.get(requ_str + "/person/" + str(id) + api_key)
        result = resp.json()
        print(id)
        id += 1
        if (resp.status_code != 200):
            print("Invalid url")
            continue
        print(result)
        act_name = result["name"]
        sql = "INSERT INTO actors(id_tmdb, name, bio, image) VALUES(" + \
        str(result["id"]) + ",\"" + str(result["name"]).replace("\"", "'") + "\",\"" + \
        str(result["biography"]).replace("\"", "'").replace("%", "%%") + "\",'" + \
        str(result["profile_path"]) + "') "
        if (result["known_for_department"] == "Acting"):
            conn.execute(sql)
        if (result["known_for_department"] == "Directing"):
            conn.execute(sql.replace("actors(id_", "directors(id_"))
        time.sleep(1)


def update_films_directors(conn, result, crew, lines):
    sql = "INSERT INTO films_directors(fk_films, fk_directors) VALUES("
    if (lines):
        (max_id_movies,) = lines[0]
        sql += str(max_id_movies)
    sql += ",\""
    for i in crew:
        if (i["department"] == "Directing"):
            lines = conn.execute("SELECT id FROM directors WHERE id_tmdb = " + str(i["id"])).fetchall()
            if (lines):
                (id_actors,) = lines[0]
                sql += str(id_actors) + ","
            else:
                add_one_person(requ_str, api_key, conn, str(i["id"]))
                lines = conn.execute("SELECT id FROM directors WHERE id_tmdb = " + str(i["id"])).fetchall()
                (id_actors,) = lines[0]
                sql += str(id_actors) + ","
    if (sql[-1] == ','):
        sql = sql[:-1]
    sql += "\")"
    conn.execute(sql)


def update_films_actors(conn, result, cast, lines):
    sql = "INSERT INTO films_casting(fk_films, fk_actors) VALUES("
    if (lines):
        (max_id_movies,) = lines[0]
        sql += str(max_id_movies)
    sql += ",\""
    for i in cast:
        lines = conn.execute("SELECT id FROM actors WHERE id_tmdb = " + str(i["id"])).fetchall()
        if (lines):
            (id_actors,) = lines[0]
            sql += str(id_actors) + ","
        else:
            add_one_person(requ_str, api_key, conn, str(i["id"]))
            lines = conn.execute("SELECT id FROM actors WHERE id_tmdb = " + str(i["id"])).fetchall()
            (id_actors,) = lines[0]
            sql += str(id_actors) + ","
    if (sql[-1] == ','):
        sql = sql[:-1]
    sql += "\")"
    conn.execute(sql)


def update_films_genres(conn, result, lines):
    genres = list(result["genres"])
    sql = "INSERT INTO films_genres(fk_films, fk_genres) VALUES("
    if (lines):
        (max_id_movies,) = lines[0]
        sql += str(max_id_movies)
    sql += ",\""
    for i in genres:
        lines = conn.execute("SELECT id FROM genres WHERE id_tmdb = " + str(i["id"])).fetchall()
        if (lines):
            (id_genre,) = lines[0]
            sql += str(id_genre) + ","
    if (sql[-1] == ','):
        sql = sql[:-1]
    sql += "\")"
    conn.execute(sql)


def update_movies(requ_str, api_key, conn, id):
    act_name = ""
    result = requests.get(requ_str + "/movie/latest" + api_key).json()
    latest = result["title"]
    max_id_movies = 1

    while (act_name != latest):
        resp = requests.get(requ_str + "/movie/" + str(id) + api_key)
        result = resp.json()
        time.sleep(1)
        credits = requests.get(requ_str + "/movie/" + str(id) + "/credits" + api_key).json()
        print(id)
        id += 1
        if (resp.status_code != 200):
            print("Invalid url")
            continue
        print(result)
        act_name = result["title"]
        sql = "INSERT INTO films(id_tmdb, title, release_date, overview, adult, rating, image) VALUES(" + \
        str(result["id"]) + ",\"" + \
        str(result["title"]).replace("\"", "'").replace("%", "%%") + "\",\"" +\
        str(result["release_date"]) + "\",\"" + \
        str(result["overview"]).replace("\"", "'").replace("%", "%%") + "\"," +\
        str(result["adult"]) + "," + \
        str(result["vote_average"]) + ",'" + \
        str(result["poster_path"]) + "') "
        conn.execute(sql)
        time.sleep(1)
        lines = conn.execute("SELECT id FROM films ORDER BY id DESC LIMIT 1").fetchall()
        update_films_genres(conn, result, lines)
        update_films_directors(conn, result, credits["crew"], lines)
        update_films_actors(conn, result, credits["cast"], lines)


# def update_casting(requ_str, api_key, conn, id):
#     act_name = ""
#     result = requests.get(requ_str + "/person/latest" + api_key).json()
#     latest = result["name"]

#     while (act_name != latest):
#         add_one_person(requ_str, api_key, conn, id)


def update_genres(requ_str, api_key, conn, id):
    tmp = "/genre/movie/list"
    requ_obj = requests.get(requ_str + tmp + api_key)
    tag = requ_obj.json()
    genres = list(tag["genres"])
    for i in genres:
        if (int(i["id"] > id)):
            result = conn.execute("INSERT INTO genres(id_tmdb, name) VALUES(" +
            str(i["id"]) + ",'" + str(i["name"]).replace("\"", "'") + "')")
            print(i['id'], i['name'])


def get_tag_list():
    engine = create_engine('mysql+pymysql://moviepi_api:moviepi_api@51.75.141.254:3306/moviepi')
    conn = engine.connect()
    requ_str = "https://api.themoviedb.org/3"
    api_key = "?api_key=f337b9ba57004f5c9ea2785b623c0439&language=fr"
    max_id_actors = max_id_directors = max_id_movies = max_id_genres = 0

    lines = conn.execute("SELECT id_tmdb FROM genres ORDER BY id_tmdb DESC LIMIT 1").fetchall()
    if (lines):
        (max_id_genres,) = lines[0]
    update_genres(requ_str, api_key, conn, max_id_genres)
    # lines = conn.execute("SELECT id_tmdb FROM actors ORDER BY id_tmdb DESC LIMIT 1").fetchall()
    # if (lines):
    #     (max_id_actors,) = lines[0]
    # lines = conn.execute("SELECT id_tmdb FROM directors ORDER BY id_tmdb DESC LIMIT 1").fetchall()
    # if (lines):
    #     (max_id_directors,) = lines[0]
    # update_casting(requ_str, api_key, conn, max(max_id_actors, max_id_directors) + 1)
    lines = conn.execute("SELECT id_tmdb FROM films ORDER BY id_tmdb DESC LIMIT 1").fetchall()
    if (lines):
        (max_id_movies,) = lines[0]
    update_movies(requ_str, api_key, conn, max_id_movies + 1)
    conn.close()

tag_list = get_tag_list()
