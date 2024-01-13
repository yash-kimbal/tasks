import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()  # read connection parameters
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)  # ** used for  unpack dictionary, key-value pair

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
