from flask import Flask # the class Flask from the module flask
app = Flask(__name__)
from app import routes # avoids circular imports, which can happen with Flask. Routes module needs to import the app variable, so having the import at the bottom stops the two files from referencing themselves in a circle