from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Форма авторизации"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение', validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddCarForm(FlaskForm):
    """Форма добавления наушников"""
    model = StringField('Модель', validators=[DataRequired()])
    price = IntegerField('Цена(₽)', validators=[DataRequired()])
    color = StringField('Цвет', validators=[DataRequired()])
    power = StringField('Тип товара', validators=[DataRequired()])
    dealer_id = SelectField('Место продажи', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Добавить')


class AddDealerForm(FlaskForm):
    """Добавление магазина"""
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class SearchPriceForm(FlaskForm):
    """Форма поиска по цене"""
    start_price = IntegerField('Минимальная цена', validators=[DataRequired()], default=0)
    end_price = IntegerField('Максимальная цена', validators=[DataRequired()], default=100000)
    submit = SubmitField('Поиск')


class SearchDealerForm(FlaskForm):
    """Форма поиска по магазину"""
    dealer_id = SelectField('Название торговой точки', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Поиск')
