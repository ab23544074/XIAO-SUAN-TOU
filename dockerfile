FROM python:3.8.6

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /backend_code
COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD gunicorn myapp.wsgi
#CMD ["python", "manage.py", "runserver"]