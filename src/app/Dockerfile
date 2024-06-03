FROM alpine:3.10

WORKDIR /src/

COPY requirements.txt /src

RUN pip install -r requirements.txt

COPY . /src

EXPOSE 8000

CMD ["uvicorn", "main:src", "--host", "0.0.0.0", "--port", "8000"]
