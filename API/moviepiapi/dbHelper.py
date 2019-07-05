##
# EPITECH PROJECT, 2019
# MoviePi
# File description:
# dbHelper.py
##

from sqlalchemy import create_engine

###############################################################################
#                               dbHelper                                      #
###############################################################################


class dbHelper():
    _dbEngine = None
    _conn = None

    # Consructor of the class
    # Create the engine
    def __init__(self, user, password, database, address, port=3306):
        self._dbEngine = create_engine('mysql+pymysql://' + user +
                                       ':' + password + '@' + address + ':' + str(port) + '/' + database)
        self.connect()

    #Method : connect
    # Etablish connection with Movie'Pi database
    def connect(self):
        self._conn = self._dbEngine.connect()

    #Method : request
    # Simplify the request system. Execute an sql command and return the command's result
    def request(self, query, *args):
        query = self._conn.execute(query, *args)
        if query.keys() and query.cursor:
            return [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        else:
            return None

    def insert(self, query, *args):
        query = self._conn.execute(query, *args)
        return query.lastrowid
