import psycopg2 as db
conn = db.connect(host="127.0.0.1:5000  ",dbname="Restaurent",user="postgres",
                        password="babe123",post=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXIST user(
    id INT PRIMARY KEY,
    name VARCHAR(260),
    password VARCHAR(5000),
    email VARCHAR(300)
);
""")
conn.commit()
cur.close()


conn.close() 
