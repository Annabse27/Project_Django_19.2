# Skystore Django Project

## Описание
Проект Skystore - это веб-приложение на основе Django, предоставляющее платформу для хранения и продажи плагинов и примеров кода.

## Установка и настройка

### Требования
- Python 3.6+
- Django 4.2.11
- Poetry

### Установка
1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/Annabse27/Project_Django_19.2.git
    cd skystore
    ```

2. Настройте виртуальное окружение и установите зависимости с помощью Poetry:
    ```sh
    poetry install
    poetry shell
    ```

3. Создайте и настройте базу данных:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Создайте суперпользователя для доступа к административной панели:
    ```sh
    python manage.py createsuperuser
    ```

5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

6. Перейдите в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Структура проекта

```
myproject/
    ├── manage.py
    ├── myproject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── catalog/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── templates/
    │   │   └── catalog/
    │   │       ├── index.html
    │   │       └── contact.html
    │   ├── tests.py
    │   ├── views.py
    │   └── urls.py
    ├── contacts/
    │   ├── __init__.py
    │   └── urls.py
    └── db.sqlite3
```

## Маршруты
- `/` - Главная страница
- `/catalog/contacts/` - Страница контактов

## Администрирование
Для доступа к административной панели перейдите по адресу `/admin/` и войдите под учетной записью суперпользователя.

## Управление базой данных
База данных по умолчанию использует SQLite. Все миграции и настройки базы данных управляются с помощью стандартных команд Django:
- `python manage.py makemigrations` - создание новых миграций на основе изменений в моделях
- `python manage.py migrate` - применение и синхронизация миграций с базой данных

## Лицензия
Этот проект лицензирован под MIT License. Подробности см. в LICENSE файле.
