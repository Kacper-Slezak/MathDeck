from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .routes.auth import auth_bp
#from .routes.teacher import teacher_bp
#from .routes.student import student_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
#app.register_blueprint(teacher_bp, url_prefix='/teacher')
#app.register_blueprint(student_bp, url_prefix='/student')