FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python3 manage.py collectstatic && gunicorn tapasBackend.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]