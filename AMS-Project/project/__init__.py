from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'GiantRed03#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
    
