FROM alpine:latest

WORKDIR /app

RUN apk add --no-cache python3 python3-dev py3-pip ruby ruby-dev make gcc g++ libc-dev cmake openssl-dev zlib-dev icu-dev git

RUN gem install github-linguist

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3", "main.py"]

