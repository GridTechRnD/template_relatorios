FROM python:3.11.9-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk add -U make

RUN apk add -U --repository http://dl-3.alpinelinux.org/alpine/edge/main \
    poppler harfbuzz-icu

RUN apk add -U --repository http://dl-3.alpinelinux.org/alpine/edge/community \
    zziplib

RUN apk add -U --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
    texlive-full

RUN ln -s /usr/bin/mktexlsr /usr/bin/mktexlsr.pl

RUN pip install --no-cache-dir -r /app/requirements.txt 

COPY ./app /app/

CMD ["hypercorn", "api:app", "--bind", "0.0.0.0:10001"]