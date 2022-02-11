import os

IS_DEBUG = True

SQLITE_URL = 'sqlite:///../tmp/test.db'

SALT = 'my_sJHLHLHKLаваыпuper_s!alt_#4$4344'

DATABASE = {
    'drivername': os.getenv("DB_DRIVERNAME", 'postgresql+psycopg2'),
    'host': os.getenv("DB_HOST", 'localhost'),
    'port': os.getenv("DB_PORT", '5432'),
    'username': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'database': os.getenv("DB_NAME")
}