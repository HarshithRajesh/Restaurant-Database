from flask import Flask,render_template, request,url_for
import psycopg2

# conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",
#                         password="babe123",post=5432)

# cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXIST user(
#     id INT PRIMARY KEY,
#     name VARCHAR(260),
#     password VARCHAR(5000),
#     email VARCHAR(300)
# );
# """)
# conn.commit()
# cur.close()
# conn.close()

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

    return username,password,email
        

       

if __name__ == "__main__":
    app.run(debug=True)