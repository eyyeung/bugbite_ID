# model after https://towardsdatascience.com/deploying-deep-learning-models-using-tensorflow-serving-with-docker-and-flask-3b9a76ffbbda


# main py file for setting the route and deciding what to do when user interacts with the web app
from flask import Blueprint, Flask, g, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap

import os
import model

from db import get_db

app = Flask(__name__, template_folder='Template')
Bootstrap(app)

"""
Routes
"""
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # getting the loaded file
        uploaded_file = request.files['file']
        # getting the state they are from
        state = request.form['state'].lower()
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            # getting the state result
            db = get_db()
            companies = db.execute('SELECT * FROM companies WHERE state= ?',(state,)).fetchall()
            # returning the result template
            return render_template('result.html', result = result, companies = companies)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)