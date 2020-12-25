FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/onlinestore

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/onlinestore

EXPOSE 8000
# CMD ["python","manage.py","migrate"]
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]

