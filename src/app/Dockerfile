FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /src/

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /src

EXPOSE 8000
