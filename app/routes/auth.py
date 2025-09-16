from flask import Blueprint, render_template, url_for, redirect, flash
from app.forms import RegisterForm, LoginForm
from app.services.auth import create_new_user, authenticate_user
from app import db
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate_user(form.username.data, form.password.data)
        if user:
            login_user(user)
            flash('Zalogowano pomyślnie', 'success')
            if user.is_teacher:
                return render_template(url_for('teacher.dashboard'))
            else:
                return render_template(url_for('studnet.dashboard'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/register')
def register():
    from = RegisterForm()
    if form.validate_on_submit():
        is_teacher - True if form.role.data == 'teacher' else False
        create_new_user(form.username.data, form.password.data, is_teacher)
        flash('Rejestracja zakończona sukcesem. Możesz się teraz zalogować.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
