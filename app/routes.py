from flask import render_template
from app import app # routes handles the different URLS for the application. 
from app.forms import LoginForm


@app.route('/') # decorators, basically when the URLs / and /index are requested by the browser, Flask returns this function
@app.route('/index')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

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
    return render_template('index.html', title='Home', user=user, posts=posts)
