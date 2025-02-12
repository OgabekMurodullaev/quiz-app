FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN python -m venv .venv && \
    .venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [".venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
