set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py sqlflush | python manage.py dbshell