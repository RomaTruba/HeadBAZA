﻿# FlaskHeadBAZA
Аналог интернет-магазина

Реализовано:

Авторизация и регистрация пользователей. Администратор системы внесен в базу данных. Логин admin, пароль superadmin 
Внесено три магазина и 3 товара

Возможности администратора:
- добавление магазинов
- добавление товаров
- удаление товаров
- удаление магазинов

Возможности пользователя:
- просмотр информации о товарах
- фильтрация вывода по стоимости и по наличию 

Описание файлов:
index.py - основной файл веб-сервера Flask
forms.py - классы FlaskForm для авторизации, регистрации, внесения данных
models.py - модели данных в базе данных sqlite
db.py - подключение базы данных
headphones.db - файл базы данных
templates - шаблоны страниц
static - контент (скрипты, картинки)


