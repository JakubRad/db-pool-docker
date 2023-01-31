import os
from typing import List, Union

import psycopg2
from dotenv import load_dotenv
from faker import Faker
from psycopg2.extras import execute_values

from shared.utils import init_logger

load_dotenv()

logger = init_logger()


class DatabaseConnector:
    """
    Class which provides a connection to Postgres db pool.
    """

    __slots__ = ("conn", "cursor")

    def __init__(self):
        self.conn = self.get_db_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def __new__(cls, *args, **kwargs):
        """
        Following Singleton pattern to have only one instance.
        """

        if not hasattr(cls, "instance"):
            cls.instance = super(DatabaseConnector, cls).__new__(cls)
        return cls.instance

    def get_db_connection(self):
        """
        Returns db connection.
        """

        logger.info(msg=f"[get_db_connection] HIT!")

        connection_config = {
            "host": "postgres",
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "dbname": os.getenv("POSTGRES_DB"),
            "port": 5432,
        }

        connection = psycopg2.connect(**connection_config)
        connection.autocommit = True

        return connection


def select_data_from_db_table(
    table_name: str, connection, cursor, only_count: bool = False
) -> Union[List[tuple], int]:
    """
    Method which calls SELECT * from given table name provided as argument.
    """

    logger.info(
        msg=f"[select_data_from_db_table] Connection PID: {connection.get_backend_pid()}"
    )

    if only_count:
        query = f"SELECT COUNT(*) FROM {table_name};"
    else:
        query = f"SELECT * FROM {table_name} LIMIT 100;"

    cursor.execute(query=query)

    if only_count:
        return cursor.fetchone()[0]

    return cursor.fetchall()


def insert_new_data_into_db(table_name: str, connection, cursor) -> None:
    """
    Method which calls INSERT INTO for given table name provided as argument.
    """

    logger.info(
        msg=f"[insert_new_data_into_db] Connection PID: {connection.get_backend_pid()}"
    )

    fake = Faker()

    tbl_columns = [
        "user_id",
        "email",
        "first_name",
        "last_name",
    ]

    rows_to_insert = [
        (
            fake.unique.pyint(),
            fake.unique.email(),
            fake.unique.first_name(),
            fake.unique.last_name(),
        )
        for _ in range(100)
    ]

    query = f"INSERT INTO {table_name} ({','.join(tbl_columns)}) VALUES %s;"

    execute_values(cur=cursor, sql=query, argslist=rows_to_insert)
