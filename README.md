STEPS TO BUILD (WINDOWS ONLY)
-----------------------------

cd O:\HOMEPATH\repos\WILP\backendcode
python -m venv env
env\Scripts\activate
pip install djangorestframework
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
exit






NOTE: To do migration again you may have to delete below files:-
--> .\backendcode\mysite\myapi\migrations
--> db.sqlite3