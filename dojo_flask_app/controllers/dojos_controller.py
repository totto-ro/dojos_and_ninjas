from flask import render_template, redirect, request
from dojo_flask_app import app
from dojo_flask_app.models.Dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos', methods=['GET'])
def getAllDojos():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos = dojos)

@app.route('/dojos/add', methods=['POST'])
def addDojo():
    Dojo.add_dojo(request.form) 
    return redirect ('/dojos')

@app.route('/dojo/<int:id>', methods=['GET'])
def showDojoInfo(id):
    results = Dojo.get_ninjas_in_dojo(id)
    return render_template("dojo.html", dojo=results)

