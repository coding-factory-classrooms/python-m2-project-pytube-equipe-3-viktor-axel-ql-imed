# python-m2-project-pytube-equipe-3-viktor-axel-ql-imed

##  🧰 Project Setup

To install the required packages and launch the project, open a terminal with virtual environment activated and type the following commands:

```
    python3 -m pip install -r requirements.txt      # To install dependencies
    python3 manage.py runserver 8000                # Start the project at http://127.0.0.1:8000
```



## 🕵️ Environment Variables

You need to have a ```.env``` file containing all the keys and values needed.

You can refer to the ```.env.default``` file located at ```./API_Django/.env.default```. 

Create a file named ```.env``` in folder ```API_Django``` and copy-paste the keys from the ```.env.default``` file, the values should have been given to you

**Note** : the ```.env``` file should in the same folder as ```.env.default```



## 📝 Notes

Project is available on this <a href="https://pytube-backend.herokuapp.com/admin/login/?next=/admin/" target="_blank">link</a>


To install dependencies, open a terminal and run :

```
    python3 -m pip install -r requirements.txt
```

To start the project :

```
    python3 manage.py runserver 8000
```

To make migrations :

```
    python3 manage.py makemigrations
```

To apply migrations :

```
    python3 manage.py migrate
```

To generate the required package install file:

```
    pip freeze > requirements.txt
```

To create a superuser :

```
    python3 manage.py createsuperuser
```

## 🚀 Deployment

To deploy the app, merge all the code to ```main``` branch, from terminal type the following command :

```
    git push heroku main && heroku run python manage.py migrate
```

Your local user will not work by default in production as the same databse that you have locally is not running.

To create a production super admin you can type the following command :

```
    heroku run python manage.py createsuperuser
```



