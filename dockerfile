FROM python:3.12

WORKDIR  /app

COPY ./pyproject.toml   /app

RUN pip install poetry==1.8.3

RUN poetry config virtualenvs.create false

RUN poetry install

COPY .  .
RUN chmod +x main.py
CMD ["python3","-u","main.py"]