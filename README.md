# Aleksey Khadkov
## Homework 24.1

## Для подключения данных создать файл `.env`, добавить в него :

- DB_HOST=localhost  # или 127.0.0.1:8000 / хост бд
- DB_USER=postgres  # пользователь бд
- DB_PASSWORD=12345  # пароль пользователя от бд
- DB_NAME='training'  # название бд
- DB_ENGINE='django.db.backends.postgresql_psycopg2'  # подключение бд


## В файле `users/management/commands/csu.py` команда для создания суперпользователя с паролем 12345 . запустить команду `python manage.py csu`,
