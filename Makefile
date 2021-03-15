deploy-local: # defaults to http://127.0.0.1:5000/
	flask run --host=0.0.0.0 --port=8080

deploy:
	gunicorn -w 4 -b 0.0.0.0:8080 app:app