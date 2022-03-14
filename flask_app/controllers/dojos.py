from flask_app import app 

from flask import render_template, redirect, request, session, flash 

from flask_app.models.dojo import Dojo 


@app.route('/')
def index():
    return render_template("dojosurvey.html")


@app.route('/dojo/create/', methods=['POST'])
def create_dojo():
    # data = {
    #     'name': request.form['name'],
    #     'location': request.form['location'],
    #     'language': request.form['language'],
    #     'comment' : request.form['comment']
    # }
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.save(request.form)
    new_dojoid = Dojo.save(data) 
    return redirect(f'/dojo/show/{new_dojoid}/')


@app.route('/dojo/show/<int:id>/')
def show(id):
    data = {
        'id': id
    }
    return render_template('results.html', dojo = Dojo.get_one(data))


