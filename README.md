# EventManager

A simple Django web application for managing events, users, and admin workflows.

## Overview

- Built with Django 5.1
- Uses PostgreSQL as the database
- Includes user and admin login flows
- Supports task/event management and email notifications

## Requirements

- Python 3.12
- PostgreSQL
- pipenv or virtualenv

## Setup

1. Install dependencies:

```bash
pipenv install
```

2. Activate the virtual environment:

```bash
pipenv shell
```

3. Apply migrations:

```bash
python eventmanager/manage.py migrate
```

4. Run the development server:

```bash
python eventmanager/manage.py runserver
```

5. Open the app at:

```text
http://127.0.0.1:8000/
```

## Configuration

The project settings are in `eventmanager/eventmanager/settings.py`.

### Database

The default database is configured for PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TaskManager',
        'USER': 'postgres',
        'PASSWORD': 'maham@12',
        'HOST': 'localhost',
    }
}
```

### Email

The app uses Gmail SMTP for email sending:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ninjasattendance@gmail.com'
EMAIL_HOST_PASSWORD = 'oucz vsal bfxf krza'
```

> Update these values before using the app in a real environment.

## Project structure

- `Account/` — user and admin authentication, profiles
- `TaskModule/` — task/event models and views
- `template/` — Django templates for login, dashboard, and event pages
- `eventmanager/` — core Django project configuration

## Notes

- Keep `DEBUG = True` only for development.
- Change the secret key and email credentials for production use.
