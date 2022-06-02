rm db.*
rm -rf snippets/__py*
rm -rf snippets/migra*
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py makemigrations snippets
python3 manage.py migrate snippets
python3 manage.py runserver 0.0.0.0:8123


