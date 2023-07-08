import logging
import mysql.connector
import os
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from csv import reader


@dataclass
class Record:
    """
    Data class representing individual record in CSV file.

    Methods:
        get_fullname()
            Creates a 'fullname' field based on the persons 'first_name' and 'last_name'

            Returns:
                fullname: string

        get_domain()
            Splits email address into domain.

            Returns:
                domain: string
    """

    id: str = ""
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    gender: str = ""
    ip_address: str = ""

    def get_fullname(self):
        return self.first_name + " " + self.last_name

    def get_domain(self):
        return self.email.split("@")[1]


def init_logger(file):
    """
    Initialize logger for individual etl run.
    Args:
        file: string - File being processed.
    Returns:
        logger: logging.Logger()
    """
    log_file = f"{datetime.utcnow()}-etl"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: %(module)s: %(name)s: %(levelname)s: %(message)s",
        handlers=[
            logging.FileHandler(f"./logs/{log_file}.log"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    logger = logging.getLogger(file)
    logger.info("logger initiated")
    logger.info(f"logging file: {log_file}.log")

    return logger


@contextmanager
def connect_db():
    """
    Creates connection to db based on credentials passed.
    Yields:
        connection: mysql.connect()
    """
    conn = mysql.connector.connect(
        **{
            "host": os.environ["DB_HOST"],
            "database": os.environ["DB"],
            "user": os.environ["DB_USER"],
            "password": os.environ["DB_PW"],
        }
    )

    if conn.is_connected():
        logger.info("db connection established")
        yield conn
    else:
        logger.info("db connection failed")

    logger.info("closing db connection")
    conn.close()
    logger.info("db connection closed")


def create_table_if_not_exist(cursor):
    """
    Creates data table in db if table does not exist.
    SQL file is loaded from directory.
    Args:
        cursor: mysql.connection.cursor()
    """
    logger.info("confirming/creating table")
    with open("./create_table.sql", "r") as f:
        cursor.execute(f.read())


def extract(file):
    """
    Generator that reads CSV line into dataclass Record.
    Args:
        file: Name of CSV file
    Yields:
        record: Record - Record Data Class
    """
    logger.info(f"opening {file}")
    with open(file, "r") as f:
        csv = reader(f)
        next(csv)  # skip header

        for record in csv:
            yield Record(*record)

    logger.info(f"closing {file}")


def transform(record):
    """
    Takes individual record and performs transforms for data enrichment.
    Args:
        record: Record Class
    Yields:
        tx_record: tuple - Packaged payload of enriched record ready for SQL load
    """
    fullname = record.get_fullname()
    domain = record.get_domain()
    yield (
        record.id,
        record.first_name,
        record.last_name,
        record.email,
        record.gender,
        record.ip_address,
        domain,
        fullname,
    )


def load(payload, table):
    """
    Loads batched data into db table.
    Args:
        payload: List of record objects
        table: Target table to insert in database
    """
    logger.info("start db load")
    stmt = (
        f"INSERT INTO {table} (id, first_name, last_name, email, gender, ip_address, domain, fullname) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    with connect_db() as conn:
        cursor = conn.cursor()
        create_table_if_not_exist(cursor)
        logger.info("loading data to db")
        cursor.executemany(stmt, payload)
        conn.commit()
    logger.info("db load complete")


if __name__ == "__main__":
    input_file = sys.argv[1]
    logger = init_logger(input_file)
    count = 0
    db_load = []

    for record in extract(input_file):
        count += 1
        if count % 100 == 0:
            logger.info(f"transformed records: {count}")

        for tx_record in transform(record):
            db_load.append(tx_record)

    logger.info(f"inserting {len(db_load)} records")
    load(db_load, "person_records")
    logger.info("complete")
