from flask import Flask
from flask_bootstrap5 import Bootstrap
#Bootstrap(app)
app = Flask ( __name__ )
# Config options - Make sure you created a 'config.py' file.

app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

# Create database connection object
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
#db.init_app(app)

from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "login"