from flask import Flask, jsonify, request, render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash
from flask_wtf import Form
from flask_login import LoginManager
from flask_login import login_user , logout_user , current_user , login_required
from sqlalchemy.engine import Engine
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

import datetime

import os

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_pyfile('config.cfg')
app.secret_key = os.urandom(24)
app.config['MAIL_DEFAULT_SENDER'] = 'smartnet.bth@gmail.com'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

mail = Mail(app)
ts = URLSafeTimedSerializer(app.secret_key)

 def __init__(self ,name , username ,password , email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return True
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def reload_user(self, callback):
        self.username_callback = callback
        self.password_callback = callback
        return callback

@login_manager.user_loader
def load_user(id):
 return User.query.get(int(id))

@app.route('/', methods=['GET'])

def home():

        return render_template("welcome.html")
def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)
        
@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')
    user = User(request.form['name'] , request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    email= request.form['email']
    token = s.dumps(email, salt='email-confirm')
    #Email details and confirmation link
    subject = "SmartNet-Confirm your Email"
    confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True)
    html = render_template(
            'emailtemp.html',
            confirm_url=confirm_url)
    send_email(email, subject, html)
    return '<h1>The email you entered is {}.</h1>'.format(request.form['email'])
    flash('User successfully registered.Check your email for activation link')
    return redirect(url_for('home'))

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm", max_age=86400)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    return '<h1>Your account is activated!</h1>:
      
 
    return redirect(url_for('login'))
 
@app.route('/account', methods=['GET','post'])        
@login_required
def account():
    if request.method == 'POST':
#        record = row.query.get(request.form.get('username','password'))
        user=User.query.filter_by(username=request.form['username'],password=request.form['password']).first()
        user.username = request.form['newusername']
        user.password = request.form['newpassword']
        db.session.commit()
    return render_template('account.html')
    
    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        return 'Username or Password is invalid' , 'error'
        return redirect(url_for('login'))
    login_user(registered_user)
    redirect_url = request.args.get('next') or url_for('dash')
    return redirect(redirect_url)




@app.route('/dash', methods=['GET', 'POST'])
@login_required
def dash():
return render_template("dash.html")

@app.route('/statistics', methods=['GET', 'POST'])	
@login_required
def statistics():
return render_template("statistics.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
#session.modified = True
return render_template("welcome.html")
@app.route('/admin', methods=['GET','POST'])     

def admin():
           return render_template("dashadmin.html")


@app.route('/admin/nodes', methods=['GET','POST'])    
 
def nodes():
          
 return render_template("nodes.html")

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    #app.logger.debug('Body: %s', request.get_data())
    
#import logging
#log= logging.getlogger('werkzeug')
#log.setLevel(logging.ERROR)

	
if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
	app.run('0.0.0.0', 8080)
	
	
	
	



	