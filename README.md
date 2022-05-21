STEPS TO BUILD (WINDOWS ONLY)
-----------------------------

cd P:\HOMEPATH\repos\WILP\backendcode

python -m venv env

env\Scripts\activate

pip install djangorestframework (OR "pip install -r requirements.txt")

cd mysite

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser # give user as admin@local.com and password as PASSWORD123 (ALL CAPS)

python manage.py runserver

On browser open http://127.0.0.1:8000/admin

login with username admin@local.com and password PASSWORD123

On browser open http://127.0.0.1:8000/

On browser open http://127.0.0.1:8000/studentdetails

On browser open http://127.0.0.1:8000/studentdetails/1

Ctrl+C # stop server

deactivate

exit # exit ccommand prompt




NOTE: To make python requirements.txt you need following command:-
P:\HOMEPATH\repos\WILP\backendcode> pip freeze > requirements.txt
Once requirements.txt is created then installation can be done as:-
pip install -r requirements.txt




NOTE: To do migration again you may have to delete below files:-
--> .\backendcode\mysite\myapi\migrations
--> db.sqlite3
