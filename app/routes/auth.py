from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return "Strona logowania"

@auth_bp.route('/register')
def register():
    return "Strona rejestracji"