FROM alpine:latest
WORKDIR /code
COPY ./middleware .
RUN apk update
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add --no-cache --update python3 py3-pip
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt --no-cache-dir
EXPOSE 5000
EXPOSE 27017
EXPOSE 5672
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "--log-level=debug", "wsgi:app"]