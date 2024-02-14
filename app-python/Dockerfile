FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8181"]
