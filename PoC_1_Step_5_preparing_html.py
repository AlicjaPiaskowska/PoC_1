from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3
import json
import collections

db=sqlite3.connect('PoC_1_wroclaw_mpk.db')
cursor = db.cursor()
cursor.execute('select city_name from `cities.csv`')

cities = []
for row in cursor:
    for field in row:
        cities.append(field)
#print(cities)


#create json format from SQL
cursor2 = db.cursor()
cursor2.execute('select * from `routes.csv`')
rows = cursor2.fetchall()

routes = []
for row in rows:
    routes_data = (row[0], row[1], row[2])
    routes.append(routes_data)
routes_data_list = json.dumps(routes_data)


objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["route_id"] = row[0]
    d["route_short_name"] = row[1]
    d["route_desc"] = row[2]
    objects_list.append(d)

#routes_data_json = json.dumps(objects_list, indent = 4)


    # with open("json_test.js", "w") as f:
    #     f.write(routes_data_json)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def dropdown():
    return render_template('index.html', city=cities)


@app.route('/', methods=['GET'])
def json_data():
    objects_list=objects_list
    return render_template("index.html", objects_list=objects_list)




if __name__ == "__main__":
    app.run(debug = True)