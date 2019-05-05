#!/usr/bin/env python
from flask import Flask, jsonify, request
app = Flask(__name__)

import mysql.connector
from mysql.connector import Error
import threading
import time

conn = mysql.connector.connect(database = "watsense", user = "watsense", password = "Anmol2882", host = "watsense.cswl7lqcb2fz.us-east-1.rds.amazonaws.com", port = "3306")
print ('Opened database successfully')
cur = conn.cursor()

        



# @app.route('/', methods=['GET'])
# def test():
#     return jsonify({'message': 'It works'})

@app.route('/', methods=['GET'])
def ow():
    global cur
    cur.execute("SELECT * from watsense")
    rows = cur.fetchall()
    data = []
    for row in rows:
        print(row)
        percentage = str(row[0])
        data += [{'percentage':percentage}]
    return jsonify(data)
dt = []


if __name__ == '__main__':
    app.run(debug=True)
    
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="80")




