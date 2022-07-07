"# thread-linker" 

Social Media Website written in Django.

## HTML and CSS styles have been downloaded from the internet and and were changed by me instead of creating templates from scratch 

#### Setup

1. install python-3.10.0

```bash
pip install -r /path/to/requirements.txt
```


#### Then run the server with

```bash
python manage.py runserver
```

#### Authentication

- CustomUserManager that inherits from BaseUserManager with that realized authentication with email.
- In other authentication is defoult for django.

#### DB
- During development used sqlite3
- For publishing on Heroku used PostgreSQL

#### Uploading files
- Used Cloudinary storage for uploading files on server


