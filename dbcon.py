import psycopg2
from config import config


def make_con(sql):
    """make_con keeps the connecter fucntion in a seperate .py file from the main class."""

    try:
        conn = psycopg2.connect(
        host="db.serverhost.com",
        database="defaultdb",
        user="name",
        password="secret")
        # create a cursor
        cur = conn.cursor()
	    # execute a statement
        cur.execute(sql)
	    # close the communication with the PostgreSQL
        cur.close()
        return "record inserted"
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    sql = 'SELECT version()'
    connect(sql)
