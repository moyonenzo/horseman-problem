SERVICE = api

build:
	docker compose build

up:
	docker compose up -d ${SERVICE}

down:
	docker compose down

lint:
	docker run --rm --volume ./:/src --workdir /src pyfound/black:latest_release black --check .

format:
	docker run --rm --volume ./:/src --workdir /src pyfound/black:latest_release black .

shell:
	docker compose up -d ${SERVICE} && \
	docker compose exec -it ${SERVICE} bash

logs:
	docker compose logs -f ${SERVICE}

re: down build up