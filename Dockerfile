FROM python:3.8-slim-buster

WORKDIR /shorty

COPY pyproject.toml pyproject.toml
RUN pip3 install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . .

CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8080", "--name", "shorty", "run:app"]