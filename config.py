from flask import Flask, Blueprint
from flask_mysqldb import MySQL
from flask_restful import Api
from flask_cors import CORS



app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
CORS(app)


# Config

# MYSQL
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'team40'
app.config['MYSQL_PASSWORD'] = 'Password12345!'
app.config['MYSQL_DB'] = 'moodportfolio'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp)