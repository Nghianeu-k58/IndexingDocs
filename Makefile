run-test:
	docker-compose run --rm app sh -c \
		"	flake8 src/rag tests && \
			python src/rag/dataaccess/migrations/elasticsearch/wait_for_elastic.py && \
			coverage run -m pytest tests/rag -v && \
			coverage report"

check-black:
	docker-compose run --rm app sh -c \
		"black src/rag && black tests/rag"

build:
	docker-compose build 

up:
	docker-compose up -d

down:
	docker-compose down

check-flake8:
	docker-compose run --rm app sh -c "flake8 src/rag tests" 

log-elastic:
	docker-compose logs -f elasticsearch

migrate:
	docker-compose run --rm app sh -c "python src/rag/dataaccess/migrations/elasticsearch/migrate.py"