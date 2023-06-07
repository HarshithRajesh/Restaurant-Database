# import psycopg2 as db

# DB_NAME = "postgres"
# DB_USER = "postgres"
# DB_HOST = "localhost"
# DB_PASSWORD = "babe123"
# conn = db.connect(host=DB_HOST,dname=DB_NAME,user=DB_USER,
#                         password=DB_PASSWORD,post=5432)


# def data():
#     cur = conn.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXIST user(
#         id INT PRIMARY KEY,
#         name VARCHAR(260),
#         password VARCHAR(5000),
#         email VARCHAR(300)
#     );
#     """)
#     conn.commit()
#     cur.close()


#     conn.close() 
# data()

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=Restaurent user=postgres password=babe123")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()