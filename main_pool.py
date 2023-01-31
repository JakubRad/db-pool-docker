import sys
from random import randrange
from time import sleep

from shared.database import select_data_from_db_table, insert_new_data_into_db
from shared.database_pool import get_db_pool_connection
from shared.utils import init_logger

logger = init_logger()


def main():
    """
    Main function of module.
    """

    ATTEMPTS = 5

    TABLE_NAME = "users"

    with get_db_pool_connection() as (connection, cursor):
        while ATTEMPTS >= 1:
            sleep_sec = randrange(1, 10)

            # check for existing data
            data = select_data_from_db_table(
                connection=connection, cursor=cursor, table_name=TABLE_NAME
            )

            logger.info(msg=f"[main_pool][data] DB Data: {len(data)}")

            # add new data to table
            insert_new_data_into_db(
                connection=connection, cursor=cursor, table_name=TABLE_NAME
            )

            # random sleep
            logger.info(msg=f"[main_pool][sleep] Sleeping for: {sleep_sec}")

            # attempts left
            logger.info(msg=f"[main_pool][attempts] Attempts left: {ATTEMPTS}")

            # db count query after each insert
            db_count = select_data_from_db_table(
                table_name=TABLE_NAME,
                connection=connection,
                cursor=cursor,
                only_count=True,
            )

            logger.info(msg=f"[main_pool][db_count] DB Data Count: {db_count}\n")

            ATTEMPTS -= 1

            sleep(sleep_sec)


if __name__ == "__main__":
    sys.exit(main())
