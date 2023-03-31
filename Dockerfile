FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8800"]
