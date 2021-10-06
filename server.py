from flask import Flask
from dojo_flask_app import app
from dojo_flask_app.controllers import ninjas_controller, dojos_controller











if __name__ == "__main__":
    app.run( debug = True )