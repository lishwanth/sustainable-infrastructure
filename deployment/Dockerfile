FROM python:3.9-slim

WORKDIR /app

COPY ./src /app/src
COPY ./models /app/models
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
