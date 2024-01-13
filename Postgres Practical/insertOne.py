# psycopg is a PostgreSQL  database adapter for the Python  programming language.
# import psycopg2
# from config import config
#
#
# def insert_one(id, name, phone, pincode):
#     query = """
#      INSERT INTO employee
#      VALUES ('{0}, '{1}, '{2} ,'{3});
#      """
#     conn = None
#     try:
#         params = config()
#         print("🔃Reading Database Configurations")
#         conn = psycopg2.connect(**params)
#         print("💾Connecting to Postgres")
#         cur = conn.cursor()
#         cur.execute(query.format(id, name, int(phone), int(pincode)))
#         conn.commit()
#         print("✅Commit Success😀")
#         cur.close()
#         print("🔒Connection CLose")
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# if __name__ == '__main__':
#     insert_one(112, 'Jay Sharma', 965441071, 12106)


# psycopg is a PostgreSQL  database adapter for the Python  programming language.
#
import psycopg2
from config import config


def insert_one():
    query = """
     INSERT INTO employee
     VALUES (112,'Jau Arora',78777677,99898);
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
    insert_one()
