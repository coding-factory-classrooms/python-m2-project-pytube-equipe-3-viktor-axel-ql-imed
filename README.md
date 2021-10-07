# python-m2-project-pytube-equipe-3-viktor-axel-ql-imed

## 📝 Notes

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

To apply migrations :

```
python3 manage.py migrate
```

## 🚀 Deployment

To deploy the app, merge all the code to main branch, from terminal type the following command : 

```
    git push heroku main && heroku run python manage.py migrate
```