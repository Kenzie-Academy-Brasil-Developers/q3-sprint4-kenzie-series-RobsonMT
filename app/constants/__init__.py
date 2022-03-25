SERIE_COLUMNS = ["id","serie", "seasons","released_date","genre","imdb_rating"]

EXPECTED_KEYS = SERIE_COLUMNS[1::]

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS ka_series (
        id  BIGSERIAL PRIMARY KEY, 
        serie VARCHAR(100) NOT NULL UNIQUE,
        seasons INTEGER NOT NULL,
        released_date DATE NOT NULL,
        genre VARCHAR(50) NOT NULL,
        imdb_rating FLOAT NOT NULL
    );
"""