from flask import Flask,render_template,request

import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "noorjahan@123MD",
    database = "emp"
)

if db.is_connected():
    print("MySQL connected successfully")

cursor = db.cursor()

cursor.execute("SHOW TABLES")

for tables in cursor.fetchall():
    print(tables)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/details",methods = ["GET","POST"])
def details():
    if request.method == "POST":
        emp_id = request.form["emp_id"]
        name = request.form["name"]
        age = request.form["age"]
        salary = request.form["salary"]
        dept = request.form["dept"]

        cursor = db.cursor()

        query = """
        INSERT INTO emp_details(emp_id,name,age,salary,dept) VALUES(%s,%s,%s,%s,%s)
        """

        values = (emp_id,name,age,salary,dept)

        cursor.execute(query,values)

        db.commit()

        cursor.close()

        return "message successfully saved"
    return render_template("details.html")

@app.route("/employees")
def employees():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM emp_details")

    employees = cursor.fetchall()

    cursor.close()

    return render_template("employees.html", employees=employees)

if __name__ == "__main__":
    app.run(debug = True)