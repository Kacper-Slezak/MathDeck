from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    """Formularz rejestracji nowego użytkownika."""
    username = StringField(
        'Nazwa użytkownika',
        validators=[DataRequired(), Length(min=4, max=25)]
    )
    password = PasswordField(
        'Hasło',
        validators=[DataRequired(), Length(min=8)]
    )
    confirm_password = PasswordField(
        'Potwierdź hasło',
        validators=[DataRequired(), EqualTo('password', message='Hasła muszą być identyczne')]
    )
    email = StringField(
        'Email',
        validators=[DataRequired()]
    )
    role = SelectField(
        'Rola',
        choices=[('student', 'Uczeń'), ('teacher', 'Nauczyciel')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Zarejestruj się')

    def validate_username(self, username):
        """Weryfikacja unikalności nazwy użytkownika."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ta nazwa użytkownika jest już zajęta. Wybierz inną.')


class LoginForm(FlaskForm):
    """Formularz logowania."""
    username = StringField(
        'Nazwa użytkownika',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Hasło',
        validators=[DataRequired()]
    )
    submit = SubmitField('Zaloguj się')