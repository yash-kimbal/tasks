import psycopg2
from config import config


def create_table():
    commands = (
        """
        CREATE TABLE employee(
             empID INTEGER PRIMARY KEY,
             empName varchar(10),
             empPhoneNo INTEGER UNIQUE,
             empPincode INTEGER NOT NULL
        )
        """,
    )
    conn = None
    try:
        # reading conn parameters
        params = config()
        print("Connecting....")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print("Executing Commands....")
        # creating table
        for command in commands:
            cur.execute(command)
        print("Commands Executed")
        # closing...
        cur.close()
        print("Closing Connection....")
        # commit
        conn.commit()
        print("Changes Committed....")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()
