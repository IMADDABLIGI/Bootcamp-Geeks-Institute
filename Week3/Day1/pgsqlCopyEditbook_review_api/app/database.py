import psycopg2
from config import HOSTNAME, USERNAME, PASSWORD, DATABASE

def get_db_connection():
    return psycopg2.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        dbname=DATABASE
    )