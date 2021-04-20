from flask import Flask, render_template,request,redirect,flash
from  mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


app =Flask (__name__)
app.secret_key = "keep it secret"

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create', methods= ['POST'])
def create_email():  
    if not EMAIL_REGEX.match(request.form['emails_']):
        flash("Invalid email address!")
        return redirect('/')
    query = "INSERT INTO emails (em) VALUES (%(email)s);"
    data = {
        'email': request.form['emails_']
    }
    db= connectToMySQL('email')
    emails=db.query_db(query,data)
    return redirect ('/success')




@app.route('/success')
def success():
    mysql= connectToMySQL('email')
    mail = mysql.query_db('SELECT * FROM emails;')
    print(mail)
    return render_template ("success.html", email=mail)



if __name__=="__main__":
    app.run(debug=True)
