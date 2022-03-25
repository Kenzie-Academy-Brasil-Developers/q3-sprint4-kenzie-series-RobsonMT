from app.models import DatabaseConnector
from psycopg2 import sql


class Serie(DatabaseConnector):
    def __init__(self,**kwargs) -> None:
        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]
       
    def create_new(self):
        self.get_conn_cur()

        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        values = tuple(self.__dict__.values())

        self.cur.execute(query, values)

        self.conn.commit()

        inserted_serie = self.cur.fetchone()

        self.cur.close()
        self.conn.close()

        return inserted_serie

    @classmethod
    def read_series(cls):
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        serie = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return serie

    @classmethod
    def read_by_id(cls, serie_id: int):
        cls.get_conn_cur()

        sql_user_id = sql.Literal(serie_id)

        query = sql.SQL(
            "SELECT * FROM ka_series WHERE id={id};"
        ).format(id=sql_user_id)

        cls.cur.execute(query)

        serie = cls.cur.fetchone()

        cls.cur.close()
        cls.conn.close()

        return serie