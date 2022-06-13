"""
    Источник: https://webdevblog.ru/realizaciya-shablona-singleton-v-python/?
"""
import sqlite3


class MetaSingleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Database(metaclass=MetaSingleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
        return self.connection

    def commit(self):
        return self.connection.commit

    def cursor(self):
        return self.connection.cursor

    def close(self):
        return self.connection.close



with Database().connect() as con1:
    with Database().connect() as con2:

        cursor1 = con1.cursor()
        cursor2 = con2.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS tbl (id INT PRIMARY KEY, txt TEXT);
        """
        cursor1.execute(query)
        con1.commit()

        query = """
            DELETE FROM tbl;
        """
        cursor1.execute(query)
        con1.commit()

        query = """
            INSERT INTO tbl (id, txt) VALUES (1, 'aaa');
        """
        cursor2.execute(query)
        con2.commit()

        query = """
            SELECT * FROM tbl;
        """
        cursor1.execute(query)
        res = cursor1.fetchall()
        print(res)






