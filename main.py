from flask import Flask,render_template, request,url_for
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

conn = psycopg2.connect(dbname='Restaurent', user='postgres' ,password='babe123')

cur = conn.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS user_info (
    id int PRIMARY KEY,
    name VARCHAR(260),
    password VARCHAR(5000),
    email VARCHAR(300)
)   '''
cur.execute(create_table)
conn.commit()
cur.close()
conn.close()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["GET","POST"])
def login():
   if request.method=="POST":
       username = request.form.get('user')
       password = request.form.get('pass')

       return username,password

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get("user")
        password = request.form.get("pass")
        email = request.form.get("email")
        password = generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)

        user_data = '''INSERT INTO user_info(name, password,email)
VALUES (username, password, email);
        '''
        cur = conn.cursor()
        cur.execute(user_data)
        conn.commit()
        cur.close()
        conn.close()


    return username,password,email
        

       

if __name__ == "__main__":
    app.run(debug=True)