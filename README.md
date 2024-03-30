
# Trippy

Trippy is a Real Time Web Application which allows us to Search for Lowest Prices offered by Hotels of desired cities. It Allows Users to Compare Prices of Hotels Across various OTA Platforms and Choose the one with the lowest price offered

> This project is under development, not recommended for use in production directly.

## Hotel API 

Register here for Hotels API key

[makcorps.com](https://www.makcorps.com)


## API Reference

#### Get Hotels

```http
  GET /api/${destination}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `destination`      | `string` | **Required**. destination name |



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_USERNAME`

`API_PASSWORD`

`SECRET_KEY`


## FAQ

#### What is API_USERNAME ?

It is a username that is provided when you register with the hotel api

#### What is API_PASSWORD ?
It is a password that is provided when you register with the hotel api



## Screenshots

![App Screenshot](screenshots/image2.png)

![App Screenshot](screenshots/image8.png)

## My Dream Django Project Structure ":)"
project_name/
├── config/                 # Configuration files
│   ├── settings.py         # Django settings module
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI application entry point
├── project_name/           # Django project directory
│   ├── __init__.py         # Initialization file
│   ├── asgi.py             # ASGI application entry point
│   ├── settings/           # Settings modules for different environments
│   │   ├── __init__.py
│   │   ├── base.py         # Base settings
│   │   ├── development.py  # Development settings
│   │   ├── production.py   # Production settings
│   │   └── local.py        # Local settings (not committed to version control)
│   ├── urls.py             # URL configuration for the project
│   └── wsgi.py             # WSGI application entry point
├── apps/                   # Django apps directory
│   ├── app1/               # App 1 directory
│   │   ├── migrations/     # Database migrations for app 1
│   │   ├── templates/      # HTML templates for app 1
│   │   ├── static/         # Static files (CSS, JavaScript, etc.) for app 1
│   │   ├── __init__.py
│   │   ├── admin.py        # Admin configurations for app 1
│   │   ├── models.py       # Models for app 1
│   │   ├── views.py        # Views (controller) for app 1
│   │   ├── urls.py         # URL configurations for app 1
│   │   └── tests.py        # Tests for app 1
│   ├── app2/               # App 2 directory (similar structure to app 1)
│   ├── ...                 # Other apps
├── static/                  # Project-wide static files
├── templates/               # Project-wide HTML templates
├── media/                   # User-uploaded files
├── logs/                    # Log files
├── requirements.txt         # Python dependencies
├── manage.py                # Django's command-line utility
├── scripts/                 # Custom scripts
└── README.md                # Project documentation


