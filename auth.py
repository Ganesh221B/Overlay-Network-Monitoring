  Users API for authentication
  
from flask import ( render_template, current_app, request,
  flash, url_for, redirect, session, abort, jsonify)
   
from flask.ext.login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from ..common import Response
from ..extensions import db

from ..users import User, SignupForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.route('/verify_auth', methods=['GET'])

@login_required

def verify_auth():  
   return Response.make_data_resp(data=current_user.to_json())

@auth.route('/login', methods=['POST'])
def login():
   if current_user.is_authenticated():
  return Response.make_success_resp(msg="You are already logged in")
  
   form = LoginForm()
   if form.validate_on_submit():
  user, authenticated = User.authenticate(form.login.data,
  form.password.data)
  if user :

  if authenticated:
    login_user(user, remember=form.remember_me.data)
  
    return Response.make_data_resp(data=current_user.to_json(), msg="You have successfully logged in")
 
 else:
    
    return Response.make_error_resp(msg="Invalid username or password", type="Wrong Authentication", code=422)

 else:
 
    return Response.make_error_resp(msg="Username does not exist", type="Wrong Authentication", code=422)

   return Response.make_form_error_resp(form=form)