import psycopg2
from config import config


def get_employee_data():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM employee")
        print("Total Number of Records:", cur.rowcount)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_employee_data()
