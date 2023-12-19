# Aleksey Khadkov
## Homework 25.1

## Для подключения данных создать файл `.env`, добавить в него :

- DB_HOST=localhost  # или 127.0.0.1:8000 / хост бд
- DB_USER=postgres  # пользователь бд
- DB_PASSWORD=12345  # пароль пользователя от бд
- DB_NAME='training'  # название бд
- DB_ENGINE='django.db.backends.postgresql_psycopg2'  # подключение бд


## В файле `users/management/commands/csu.py` команда для создания суперпользователя с паролем 12345 . запустить команду `python manage.py csu`,

## Создайте тестового пользователя `python manage.py ctu`

## По очереди загрузите данные курсов , уроков и платежей :

- `python manage.py loaddata courses_data.json`
- `python manage.py loaddata lessons_data.json`
- `python manage.py loaddata payment_data.json`

## Для сортировки и поиска подставлять следующие значения :

- `?ordering=-date_payment`  # сортировка по дате по убыванию.
- `?course_pay=1-2`  # сортировка по оплате конкретного курса.
- `?lesson_pay=1-4`  # сортировка по оплате урока.
- `?payment_method=наличные`  # сортировка по способу оплаты наличными.
- `?payment_method=перевод`  # сортировка по способу оплаты переводом.


## Для работы с платежеми нужен пользователь со статусом `персонала`
## Для получения токена.  `users/api/token/`: {"email": "test@sky.pro","password": "12345"}.
## Добавьте в группу `moderator` пользователя