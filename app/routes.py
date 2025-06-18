from flask import render_template, redirect, flash, url_for, request
from app import app, db # routes handles the different URLS for the application. 
from app.forms import LoginForm, RegistrationForm
import sqlalchemy as sa
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data): # catch if the user is not valid
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '': # catch if user tries to access without being logged in
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/') # decorators, basically when the URLs / and /index are requested by the browser, Flask returns this function
@app.route('/index')
def index():
    user = {'Username': 'Nestor'}
    posts = [
        {
            'author': {'username': 'Winston'},
            'body': 'Beautiful day in the town!'
        },
        {
            'author': {'username': 'Winston\'s pessimistic friend'},
            'body': 'I did not care for the Godfather.'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)
@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)