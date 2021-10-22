default:

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

superuser:
	python3 manage.py createsuperuser --username admin --email admin@via-internet.de

run:
	uvicorn main:app --reload --port 5000 --host 0.0.0.0
