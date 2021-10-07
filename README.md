# python-m2-project-pytube-equipe-3-viktor-axel-ql-imed

## 📝 Notes


Project is available on this <a href="https://pytube-backend.herokuapp.com/admin/login/?next=/admin/" target="_blank">link</a>

To install dependencies, open a terminal and run :

```
    python3 -m pip install -r requirement.txt
```

To start the project :

```
    python3 manage.py runserver 8000
```

To make migrations :

```
    python3 manage.py makemigrations
```

To create a superuser :

```
    python3 manage.py createsuperuser
```

To apply migrations :

```
    python3 manage.py migrate
```

## 🚀 Deployment

To deploy the app, merge all the code to main branch, from terminal type the following command :

```
    git push heroku main && heroku run python manage.py migrate
```

Your local user will not work by default in production as the same databse that you have locally is not running.

To create a production super admin you can type the following command : 

```
    heroku run python manage.py createsuperuser
```
