# flask-api-template
This is an example Flask App that uses a sample SQLite database as the backend database.  It can also be extended to connect to other databases such as Postgres.
##### To Run App:
1. Clone repo
2. Set up virtual python environment and install requirements.txt
3. Run `python ./utils/db/init_db.py` to create the SQLite DB.
4. Run App locally by running `gunicorn --bind 0.0.0.0:8081 main:rest_app`

Or build a docker image using `docker-compose build` and run the image using `docker-compose up -d`
