# model after https://towardsdatascience.com/deploying-deep-learning-models-using-tensorflow-serving-with-docker-and-flask-3b9a76ffbbda


# main py file for setting the route and deciding what to do when user interacts with the web app
from flask import Blueprint, Flask, g, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask import jsonify

import os
import model

from db import get_db

app = Flask(__name__, template_folder='Template')
Bootstrap(app)

# a route for ajax to connects to and updates the county in that state
@app.route('/state', methods=['POST'])
def state():
    ret = ''
    state = request.form['state']
    db = get_db()
    counties = db.execute('SELECT county FROM counties WHERE state= ?',(state,)).fetchall()        
    #counties=['a','b','c',state]
    for entry in counties:
        ret += '<option value="{}">{}</option>'.format(entry[0],entry[0])
    return ret

"""
Routes
"""
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # getting the loaded file
            uploaded_file = request.files['file']
            # getting the state and county they are from to provide info about pest control companies
            state = request.form['state']
            county = request.form['county']

            # only there is a file that we go to the result page
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
                companies = db.execute('SELECT * FROM companies WHERE state=? AND county= ?',(state,county,)).fetchall()
                # get the product category belonging to the bug
                #categories = db.execute('SELECT category FROM bug_category WHERE bug= ?',(class_name,)).fetchall()
                situations_categories = db.execute('SELECT situation,category FROM bug_category WHERE bug= ?',(class_name,)).fetchall()
                
                # make empty list and then extend to combine the products
                conditions = []

                for row in situations_categories:
                    category = row[1]
                    product = db.execute('SELECT * FROM products WHERE category = ? ORDER BY RANDOM() LIMIT 1',(category,)).fetchall()
                    conditions.append([row[0],category,product])

                # returning the result template
            return render_template('result.html', result = result, companies = companies, conditions = conditions)    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)