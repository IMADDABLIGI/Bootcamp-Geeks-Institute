import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'hicham'
PASSWORD = 'root'
DATABASE = 'dvdrental'


def connect_to_database():
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

    cursor = connection.cursor()

    query = "SELECT * FROM language LIMIT 1;"

    cursor.execute(query)

    result = cursor.fetchall()

    connection.close()
    for tuple in result:
        for item in tuple:
            print("-> ", item)




if __name__ == "__main__":
    connect_to_database()


# Result:  [(1, 'English             ', datetime.datetime(2006, 2, 15, 10, 2, 19))]




