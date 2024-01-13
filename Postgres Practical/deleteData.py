# psycopg is a PostgreSQL  database adapter for the Python  programming language.
#
import psycopg2
from config import config


def delete():
    query = """
     DELETE FROM employee
     WHERE empid=112;
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
        conn.commit()
        print("✅Commit Success😀")
        cur.close()
        print("🔒Connection CLose")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    delete()
