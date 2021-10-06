# endpoints related to the ninjas

from flask import render_template, redirect, request
from dojo_flask_app import app
from dojo_flask_app.models import Ninja
from dojo_flask_app.models import Dojo

@app.route('/ninjas', methods=['GET'])
def chooseDojo():
    return render_template("ninja.html", dojos = Dojo.Dojo.get_all_dojos())


@app.route('/ninjas/add', methods=['POST'])
def addNinja():
    Ninja.Ninja.add_ninja(request.form) 
    print(Ninja.Ninja)
    return redirect ('/dojos')