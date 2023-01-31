import os
from contextlib import contextmanager

from dotenv import load_dotenv
from psycopg2 import pool

from shared.utils import init_logger

load_dotenv()

logger = init_logger()


@contextmanager
def get_db_pool_connection():
    """
    Returns db pool connection.
    """

    db_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        host="postgres",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=5432,
    )

    connection = db_pool.getconn()

    cursor = connection.cursor()

    try:
        yield connection, cursor
    finally:
        cursor.close()
        db_pool.putconn(connection)
