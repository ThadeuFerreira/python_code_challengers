
from multiprocessing import connection
import psycopg2
#Connect to localhost docker postgress
def connect():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "postgres",
                                      host = "localhost",
                                      port = "5432",
                                      database = "postgres")
        cursor = connection.cursor()
        print("Connection to postgress was successful!")
        return cursor, connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

#List all tables in the database
def list_tables(cursor):
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(table[0])

#Create a table of users
def create_user_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)")
    print("Table users created!")

def create_clients_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS clients (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, surname VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, username VARCHAR(50) NOT NULL)")
    print("Table clients created!")

#Add users to the table
def add_users(cursor):
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user')")
    print("Users added to table users!")

#list users from trable users
def list_users(cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Users in table users:")
    for user in users:
        print(user)

def add_client_to_table(cursor, client):
    cursor.execute("INSERT INTO clients (name, surname, email, username) VALUES (%s, %s, %s, %s)", (client.name, client.surname, client.email, client.username))
    print("Client added to table clients!")

def list_table(cursor, table_name):
    cursor.execute("SELECT * FROM %s" % table_name)
    rows = cursor.fetchall()
    print("Rows in table clients:")
    for r in rows:
        print(r)   

class Client:
    def __init__(self, name, surname, username, email: str):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email

cursor, connection = connect()

list_tables(cursor)
create_user_table(cursor)
create_clients_table(cursor)
add_users(cursor)
list_tables(cursor)
list_users(cursor)

client = Client("John2", "Doe", "johndoe", "johndoe.gmail.com")

add_client_to_table(cursor, client)
list_table(cursor, "clients")

#commit changes to database
connection.commit()