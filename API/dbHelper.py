from sqlalchemy import create_engine


class dbHelper():
    _dbEngine = None
    _conn = None

    def __init__(self, user, password, database, address, port=3306):
        self._dbEngine = create_engine('mysql+pymysql://' + user +
                                       ':' + password + '@' + address + ':' + str(port) + '/' + database)

    def connect(self):
        self._conn = self._dbEngine.connect()

    def request(self, query, *args):
        self.connect()
        query = self._conn.execute(query, *args)
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result
