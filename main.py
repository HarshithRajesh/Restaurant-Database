from flask import Flask,render_template, request,url_for,flash
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

conn = psycopg2.connect(dbname='Restaurent', user='postgres' ,password='babe123')

cur = conn.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS user_info (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(260),
    PASSWORD VARCHAR(5000),
    EMAIL VARCHAR(300)
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
       conn = psycopg2.connect(dbname='Restaurent', user='postgres' ,password='babe123')
       cur = conn.cursor()

    

       return {'status':1}

@app.route("/register",methods=["GET","POST"])
def register():
    conn = psycopg2.connect(dbname='Restaurent', user='postgres' ,password='babe123')
    cur = conn.cursor()
    if request.method=="POST":
        username = request.form.get("user")
        password = request.form.get("pass")
        repass = request.form.get("repass")
        email = request.form.get("email")

        if (password==repass):
            password = generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)

            user_data = 'INSERT INTO user_info(name,password,email) VALUES (%s,%s,%s);'
            values = (username,password,email)
            
            cur.execute(user_data,values)
            conn.commit()
            cur.close()
            conn.close()
        else:
            return {'status':0}



    
@app.route("/home",methods=["POST"])
def home_page():
    return render_template("index.html")
       

if __name__ == "__main__":
    app.run(debug=True) 