FROM python:3.11.6-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:8000"]