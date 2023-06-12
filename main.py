from flask import Flask,render_template, request,url_for,flash
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

conn = psycopg2.connect(dbname='Restaurent', user='postgres' ,password='babe123')
COUNT = 3
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
            global COUNT
            COUNT+=1
            ex ='SELECT id FROM user_info ORDER BY id DESC LIMIT(1)'
            cur.execute(ex)
            last_id = cur.fetchall()
            last_id = last_id[0][0]+1
            print(last_id)
            print(type(last_id))
            user_data = 'INSERT INTO user_info(id,name,password,email) VALUES (%s,%s,%s,%s);'
            values = (last_id,username,password,email)
            print(last_id)
            cur.execute(user_data,values)
            conn.commit()
            cur.close()
            conn.close()
            redire
            return{'status':1}
        else:
            return {'status':0}



@app.route("/home",methods=["GET"])
def home_page():
    return render_template("index.html")
    # if request.method=="POST":

    #     breakfast = request.form.get("breakfast")
    #     lunch = request.form.ger("lunch")
    #     snacks = request.form.get("snacks")
    #     dinner = request.form.get("dinner")
    #     ordered= []
    #     if breakfast:
    #         ordered.append("breakfast")
    #     if lunch:
    #         ordered.append("lunch")
    #     if snacks:
    #         ordered.append("snacks")
    #     if dinner:
    #         ordered.append("dinner")
    #     else:
    #         ordered.append("null")
    
    # return ordered
        
       

if __name__ == "__main__":
    app.run(debug=True) 