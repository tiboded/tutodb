from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

#APP INSTANCE
app=Flask(__name__)
app.config['DEBUG']=True

#DATABASE
SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
        username='webrobbie',
        password='passworddb',
        hostname='webrobbie.mysql.pythonanywhere-services.com',
        databasename='webrobbie$tutodb',
        )
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_POOL_RECYCLE']=299
db=SQLAlchemy(app)
#on PythonAnywhere :
#from app import db
#db.create_all()

#MODEL
class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(128))

#ROUTE
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html',comments=Comment.query.all())
    comment=Comment(content=request.form['content'])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

