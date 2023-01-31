import sys
from random import randrange
from time import sleep

from shared.database import (
    DatabaseConnector,
    select_data_from_db_table,
    insert_new_data_into_db,
)
from shared.utils import init_logger

logger = init_logger()


def main():
    """
    Main function of module.
    """

    attempts = 5

    table_name = "users"

    with DatabaseConnector() as db_pool:
        connection = db_pool.conn

        with connection.cursor() as cursor:
            while attempts >= 1:
                sleep_sec = randrange(1, 10)

                # check for existing data
                data = select_data_from_db_table(
                    connection=connection, cursor=cursor, table_name=table_name
                )

                logger.info(msg=f"[main][data] DB Data: {len(data)}")

                # add new data to table
                insert_new_data_into_db(
                    connection=connection, cursor=cursor, table_name=table_name
                )

                # random sleep
                logger.info(msg=f"[main][sleep] Sleeping for: {sleep_sec}")

                # attempts left
                logger.info(msg=f"[main][attempts] Attempts left: {attempts}")

                # db count query after each insert
                db_count = select_data_from_db_table(
                    table_name=table_name,
                    connection=connection,
                    cursor=cursor,
                    only_count=True,
                )

                logger.info(msg=f"[main][db_count] DB Data Count: {db_count}\n")

                attempts -= 1

                sleep(sleep_sec)


if __name__ == "__main__":
    sys.exit(main())
