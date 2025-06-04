from app import app # routes handles the different URLS for the application. 

@app.route('/') # decorators, basically when the URLs / and /index are requested by the browser, Flask returns this function
@app.route('/index')
def index():
    return "Hello, World!"

