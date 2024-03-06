FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["sh", "-c", "uvicorn app.main:app --reload --port=9000 --host=0.0.0.0"]
