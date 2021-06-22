FROM python:latest

WORKDIR /app

COPY requirements_plotting.txt plotting.py ./

RUN pip install -r requirements_plotting.txt

CMD [ "python", "./plotting.py" ]

