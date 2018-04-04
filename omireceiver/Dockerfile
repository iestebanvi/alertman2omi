FROM python:3.6-alpine
MAINTAINER Andre Rozendaal "junk@bitjes.com"

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
