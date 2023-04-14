from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from config import Config
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
mysql = MySQL(app)


from app import routes
