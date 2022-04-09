from . import auth_blueprint
from myapp.auth.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, request, redirect, Blueprint, json, flash, session
from myapp.models import User
# from myapp import db, bcrypt
from myapp.models import db


@auth_blueprint.route('/')
def index():
    return render_template('auth/register.html')


@auth_blueprint.route('/login', methods=['GET','POST'])
@auth_blueprint.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        else:
            login_user(user, remember=True)
            return redirect(url_for('user.index'))
    return render_template('auth/login.html', form=form, login=True)

@auth_blueprint.route('/register', methods=['GET','POST'])
@auth_blueprint.route('/register/', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      email = form.email.data
      password = form.password.data
      user = User(email=email, confirmed=True)
      user.set_password(password)
      db.session.add(user)
      db.session.commit()
      flash('Account is registered successfully', 'success')
  return render_template('auth/register.html', form=form)