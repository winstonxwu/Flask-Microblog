from flask import render_template
from app import app # routes handles the different URLS for the application. 


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
    return render_template('index.html', title='Home', user=user, posts=posts)
