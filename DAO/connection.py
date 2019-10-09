import psycopg2


def get_connection():
    return psycopg2.connect("dbname=h2pg user=sa password='sa' host=localhost port=5435")
