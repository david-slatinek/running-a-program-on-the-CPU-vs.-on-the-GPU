FROM python:latest

WORKDIR /app

COPY requirements_main.txt main.py ./

RUN pip install -r requirements_main.txt

CMD [ "python", "./main.py" ]
