FROM djangobot:v1

WORKDIR /usr/src/app/steambot
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]