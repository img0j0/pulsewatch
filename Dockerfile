FROM python:3.10-slim

WORKDIR /app
COPY backend /app

RUN pip install flask

EXPOSE 8000
CMD ["python", "app.py"]
