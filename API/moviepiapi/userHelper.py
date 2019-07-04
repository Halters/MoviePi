##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# userHelper.py
##

import uuid
import hashlib


class userHelper():
    db = None
    LEN_MAX_USER = None

    def __init__(self, db, LEN_MAX_USER):
        self.db = db
        self.LEN_MAX_USER = LEN_MAX_USER

    def generateUUID(self):
        return uuid.uuid4()

    def hashPassword(self, password):
        password = hashlib.sha256(password.encode('utf_8'))
        password = password.hexdigest()
        return password

    def checkUsername(self, username):
        if (len(username) > self.LEN_MAX_USER):
            return False, "La limite de caractère est de " + str(self.LEN_MAX_USER)
        result = self.db.request(
            "SELECT * From users WHERE username=%s", username)
        if result:
            return False, "Le nom d'utilisateur est déjà utilisé"
        return True, "Le nom d'utilisateur est valide"

    def createNewUser(self, username, password, age):
        isValid, _ = self.checkUsername(username)
        if not isValid:
            return False
        user_uuid = self.generateUUID()
        password = self.hashPassword(password)
        queryString = "INSERT INTO users (username, age, password, uuid) VALUES (%s,%s,%s,_binary %s)"
        insert_id = self.db.insert(queryString,
                                   username, age, password, user_uuid.bytes)
        if not insert_id:
            return False
        return self.getUserInformations(user_id=insert_id)

    def setUserGenres(self, user_id, newGenres):
        self.db.request("DELETE FROM users_genres WHERE id = %s", user_id)
        for genre in newGenres:
            self.db.insert(
                "INSERT INTO users_genres (fk_users, fk_genres) VALUES (%s, %s)", user_id, genre)

    def updateUserInfos(self, user_id, username, password, age):
        if password:
            self.db.request(
                "UPDATE users SET username = %s, password = %s, age = %s WHERE id = %s", username, password, age, user_id)
        else:
            self.db.request(
                "UPDATE users SET username = %s, age = %s WHERE id = %s", username, age, user_id)
        return self.getUserInformations(user_id=user_id)

    def getUserInformations(self, user_id=None, user_uuid=None):
        queryString = "SELECT * FROM users WHERE "
        if user_id:
            queryString += "id = %s"
            result = self.db.request(queryString, user_id)
        elif user_uuid:
            queryString += " uuid = _binary %s"
            result = self.db.request(queryString, user_uuid)
        else:
            return False
        if not result:
            return None
        userInfos = result[0]
        return userInfos

    def getUserFilmsSeen(self, user_id):
        queryString = "SELECT t1.id, t1.title, t1.image FROM films AS t1 INNER JOIN users_films AS t2 ON t1.id = t2.fk_films WHERE t2.fk_users = %s"
        result = self.db.request(queryString, user_id)
        return result

    def getUserGenres(self, user_id):
        queryString = "SELECT t1.id, t1.name FROM genres AS t1 INNER JOIN users_genres AS t2 ON t1.id = t2.fk_genres WHERE t2.fk_users = %s"
        result = self.db.request(queryString, user_id)
        return result

    def getUUIDstrFromBinary(self, uuid_binary):
        return str(uuid.UUID(bytes=uuid_binary))

    def getUUIDBinaryFromStr(self, uuid_str):
        return uuid.UUID(uuid_str).bytes

    def getUserForAuth(self, username, password):
        password = self.hashPassword(password)
        user = self.db.request(
            "SELECT * FROM users WHERE username=%s AND password=%s", username, password)
        if not user:
            return False
        return user[0]
