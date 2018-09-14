FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


# Port to expose
EXPOSE 8000



CMD ["gunicorn", "--bind", "0.0.0.0:8000", "contabot.wsgi:application"]
