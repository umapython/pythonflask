# import importlib
# import mysql.connector as mysqlconn
# import mysql.connector
# import dbconf as conf

# _database='umapython'
# _host='localhost'
# _user='root'
# _passwd='admin123'
# _admin='admin'
# _admin_passwd='admin123'


# def set_profile(conf,user):
#     profile=conf.profiles.get("mysql")
#     _database=profile.get("_database")
#     _host=profile.get("_host")
#     _user=profile.get("_"+user)
#     _passwd=profile.get("_"+user+"_passwd")
#     _admin=profile.get("_admin_user")
#     _admin_passwd=profile.get("_admin_passwd")
# def getsql_dialect(conf):
#     return importlib.import_module(conf.SQL_DIAELECT_MODULE)
# def getConnection(conf):
#     return mysqlconn.connect(host=_host,user=_user,passwd=_passwd,database=_database)
import mysql.connector as mysqlconn
import importlib
from contextlib import closing
import mysql.connector
from openpyxl import Workbook, load_workbook
import pandas.io.sql as sql
import os
import math
from openpyxl.styles import colors, Color, PatternFill, Font
import mysql.connector

import re
import pandas as pd
import time
from pymysql import*
import pandas.io.sql as sql
import logging
from flask import request




_database = 'umapython'
_host = 'localhost'
_user = 'root'
_passwd = 'admin123'
_admin = 'admin'
_admin_passwd = 'admin123'


def set_profile(conf, user):
    profile = conf.profiles.get("mysql")
    _database = profile.get("_database")
    _host = profile.get("_host")
    _user = profile.get("_"+user)
    _passwd = profile.get("_"+user+"_passwd")
    _admin = profile.get("_admin_user")
    _admin_passwd = profile.get("_admin_passwd")


def getsql_dialect(conf):
    return importlib.import_module(conf.SQL_DIALECT_MODULE)


def getConnection():

    return mysqlconn.connect(host=_host, user=_user, passwd=_passwd, database=_database)