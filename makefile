run.django:
	python manage.py runserver

run.gunicorn:
	gunicorn poc.wsgi:application --bind=0.0.0.0:8000 --timeout=300 --log-level info --workers=8 --threads=4 --max-requests=500

run.gunicorn.uvicorn:
	gunicorn poc.wsgi:application --bind=0.0.0.0:8000 --timeout=300 --log-level info --workers=12 --max-requests=500 -k uvicorn.workers.UvicornWorker

run.uvicorn:
	uvicorn poc.asgi:application --log-level info --workers=1
