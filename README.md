# MyProject

MyProject — это веб-приложение на основе Django, предназначенное для управления продуктами, блоговыми постами и взаимодействием с пользователями. Этот файл README предоставляет обзор структуры проекта и основных компонентов.

## Структура проекта

```
myproject/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── signup.html
│   │       └── password_reset_form.html 
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── tests.py  # правда тестов нет
├── catalog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models/
│   │       ├── __init__.py
│   │       ├── blog.py
│   │       ├── contact_forms.py
│   │       └── product_forms.py
│   ├── forms/
│   │       ├── __init__.py
│   │       ├── blog_forms.py
│   │       ├── product.py
│   │       └── product_models.py

│   ├── views/
│   │       ├── __init__.py
│   │       ├── blog_views.py
│   │       ├── category_views.py
│   │       ├── contact_views.py
│   │       └── product_views.py
│   ├── urls.py
│   ├── templates/
│   │   └── catalog/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── другие шаблоны...
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── tests.py  # если есть тесты
├── manage.py
└── .env
```

### Основные каталоги и файлы

- **config/**: Содержит файлы конфигурации проекта.
  - `settings.py`: Основные настройки проекта, включая подключение к базе данных и конфигурацию приложений.
  - `urls.py`: Главный файл маршрутизации (роутинг) для всего проекта.
  - `wsgi.py`: Настройка для развертывания проекта на сервере.
  
- **users/**: Приложение для работы с пользователями.
  - `models.py`: Определение модели пользователя (`CustomUser`).
  - `forms.py`: Формы для регистрации, авторизации и восстановления пароля.
  - `views.py`: Представления для регистрации, входа, выхода, восстановления пароля и других действий с пользователями.
  - `urls.py`: Маршруты, связанные с пользователями.
  - `templates/users/`: Шаблоны для страниц входа, регистрации и восстановления пароля.
  
- **catalog/**: Приложение для работы с товарами или контентом.
  - `models.py`: Определение моделей для товаров, категорий и других объектов.
  - `forms.py`: Содержит определения форм для приложения.
  - `views.py`: Представления для отображения товаров и категорий.
  - `urls.py`: Маршруты, связанные с каталогом.
  - `templates/catalog/`: Шаблоны для страниц каталога.

- **media/**: Каталог для хранения загруженных медиа-файлов (изображений, документов и т.д.).

- **manage.py**: Основная команда для выполнения административных задач, таких как миграции, запуск сервера и т.д.

- **.env**: Файл с конфиденциальными данными, такими как пароли и ключи API.


## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Annabse27/Project_Django_19.2
   cd myproject
   ```

2. **Установите зависимости:**
   ```bash
   poetry install
   ```

3. Создайте файл `.env` в корне проекта и добавьте в него конфиденциальные данные (см. пример ниже):

   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
   REDIS_URL=redis://127.0.0.1:6379/1
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   DEFAULT_FROM_EMAIL=your-email@example.com
   ```

### Запуск Redis

Проект требует активного подключения к Redis для корректной работы. Запустите Redis одним из следующих способов:

- **Локально**:
  
  ```bash
  redis-server
  ```

- **Через Docker**:

  ```bash
  docker run -d -p 6379:6379 redis
  ```

### Запуск проекта

1. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

2. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.


## Использование

- Доступ к главной странице можно получить по адресу `http://localhost:8000/`.
- Для управления приложением используйте интерфейс администратора по адресу `http://localhost:8000/admin/`.
- Пользователи могут создавать и управлять продуктами, просматривать блоговые посты и взаимодействовать с формой обратной связи.

## Вклад

Вклады приветствуются! Пожалуйста, форкните репозиторий и отправьте pull request с вашими изменениями.

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности см. в файле [LICENSE](LICENSE).
