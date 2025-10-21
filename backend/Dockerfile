FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Si tes libs sont "pure python" ou utilisent psycopg2-binary, pas besoin d'outils de build
# RUN apk add --no-cache build-base   <-- supprimé

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
