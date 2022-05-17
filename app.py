
from pathlib import Path
import pandas as pd
import base64
import shutil, os
import dbconf as conf



from flask import Flask, render_template, request ,Response, jsonify, make_response
import json

from flask_cors import CORS

#import requests
import re
from urllib.parse import unquote
import time
from openpyxl import Workbook,load_workbook
import xlsxwriter
from zipfile import ZipFile
import socket
import excel2img
from datetime import date
import xlrd as xl  
import datetime
from werkzeug.utils import secure_filename

import xlwings as xw

app=Flask(__name__)
cors=CORS(app,resources={r"/*":{"origins":"*"}})

db=conf.getProvider()
db.set_profile(conf,"user")
sql_queries=db.getsql_dialect(conf)

@app.route("/register",methods=['POST'])
def Register():
    print(request.form['email'])
    newList=[]
    email=request.form['email']
    print(request.form['email'])
    password=request.form['password']
    print(password)
    username=request.form['username']
    print(username)
    contact=request.form['contact']
    print(email,password,username,contact)
    userdata=db.execute_sql(sql_queries.REGISTER_QRY,[email,password,username,contact])
    print("my userdata:",userdata)
    for data in userdata:
        newList.append(data)
    return Response(json.dumps(newList),status=201,mimetype="application/json")
        
    

if __name__=="__main__":
    app.run()
    

