from flask import Flask, session, request, render_template, redirect,url_for
from conversationengine import is_rating, message_handler as cs
from sqlalchemy import select
import sqlalchemy as db   #sql alchemy module
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)

app.secret_key = os.urandom(10)


#azure database connected for testing purposes
engine = db.create_engine("mssql+pymssql://task:Yasser13@chatbottask.database.windows.net/chatbot")
conn = engine.connect()
metdata = db.MetaData()                                                     #retrieving database metadata
Rating = db.Table('RATINGS',metdata,autoload = True,autoload_with = engine)




@app.route("/", methods = ["POST","GET"])
def Home():
    
    if request.method == "POST":
        name  = request.form['first_name']
        session['name'] = name
        session['rating'] = ''
        

        session['stage'] = 'hello'
        return redirect(url_for("chatbot"))

    return render_template("Home.html")



@app.route("/chat", methods = ["GET", "POST"])
def chatbot():
    
    if request.method == "POST":
        
        msg = (request.get_json(force=True))['message']
        stage = session['stage']
        rating = session['rating']
    
        if stage == 'hello':
            session['stage'] = cs(msg,stage)[1]             
            return cs(msg,stage)[0]
        
        elif stage == 'recommend':
            session['stage'] = cs(msg,stage)[1]

            if is_rating(msg):                  #User enters a rating -> insert to database
                rating = msg
                ins = Rating.insert().values(Name= session['name'],RATING= rating)
                conn.execute(ins)
                
 
            return cs(msg,stage)[0]

        elif stage == 'hangup':
            return render_template('Home.html'),500

    return render_template('chatbot.html',welcome = cs('hello','hello',session['name'],'Neuro.net')[0])



@app.cli.command('ratings')           #Select ALL from Ratings Table
def ratings():
    sel = select([Rating])
    result = conn.execute(sel)

    for row in result:
        print(row)
   



