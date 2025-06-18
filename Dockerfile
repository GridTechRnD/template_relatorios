FROM python:slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-xetex \
    texlive-latex-recommended && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/mktexlsr /usr/bin/mktexlsr.pl

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt 

COPY ./app /app/

CMD ["hypercorn", "api:app", "--bind", "0.0.0.0:10001"]