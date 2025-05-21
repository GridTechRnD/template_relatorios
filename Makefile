.PHONY: all clean build run deploy

all: deploy

build:
	docker-compose build

run:
	docker-compose up -d

clean:
	docker-compose down

logs:
	docker-compose logs -f

deploy: clean build run