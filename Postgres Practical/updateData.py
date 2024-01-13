# psycopg is a PostgreSQL  database adapter for the Python  programming language.
#
import psycopg2
from config import config


def insert_one():
    query = """
     UPDATE employee
     SET emppincode=12111
     WHERE empid=111
     """
    conn = None
    try:
        params = config()
        print("🔃Reading Database Configurations")
        conn = psycopg2.connect(**params)
        print("💾Connecting to Postgres")
        cur = conn.cursor()
        cur.execute(query)
        print("✔ Query Executed Successfully")
        conn.co️mmit()
        print("✅Commit Success😀")
        cur.close()
        print("🔒Connection CLose")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    insert_one()
