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




--------- FOR UBUNTU 22.04 ---------

1> Download python portable from https://github.com/squeaky-pl/portable-pypy#latest-python-36-release as 'pypy3.6-7.2.0-linux_x86_64-portable.tar.bz2'
2> extract it at a folder '$HOME/ProgramFilesAllLinux/pypy3.6-7.2.0-linux_x86_64-portable'

export PATH="$HOME/ProgramFilesAllLinux/pypy3.6-7.2.0-linux_x86_64-portable/bin:/usr/bin"

cd $HOME/repos/WILP/backendcode

pypy3 -m venv env
OR
python3 -m venv env
OR
python -m venv env

source ./env/bin/activate
OR
. ./env/bin/activate

pip install djangorestframework
OR
pip3 install djangorestframework

cd mysite

python(3) manage.py makemigrations
python(3) manage.py migrate
python(3) manage.py runserver

CTRL+C
deactivate
