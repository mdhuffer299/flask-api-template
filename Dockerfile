FROM python:3.10-alpine
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r ./requirements.txt
COPY . .
RUN python ./utils/db/init_db.py
