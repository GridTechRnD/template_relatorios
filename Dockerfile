FROM python:3.11.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt 

RUN playwright install chromium

RUN playwright install-deps chromium

COPY ./app /app/

CMD ["hypercorn", "api:app", "--bind", "0.0.0.0:10001"]