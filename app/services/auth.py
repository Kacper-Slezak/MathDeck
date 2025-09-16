# app/auth_service.py

from app.models import User
from app import db

def create_new_user(username, password, is_teacher):
    new_user = User(username=username, is_teacher=is_teacher)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None