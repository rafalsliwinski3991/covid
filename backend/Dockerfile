FROM python:3.7
ENV COVID_ENV dev
ENV PYTHONUNBUFFERED 1

EXPOSE 8888


RUN mkdir -p /src/app
WORKDIR /src/app

COPY ./backend/requirements /src/app/requirements
RUN pip install --no-cache-dir -r ./requirements/$COVID_ENV.txt

COPY . .

# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["django-admin", "startproject", "covid_backend"]
# CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]