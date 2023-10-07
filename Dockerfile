FROM python:3.11.6-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]