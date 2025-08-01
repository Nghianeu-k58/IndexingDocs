run-test:
	docker-compose run --rm app sh -c \
		"coverage run -m pytest tests/rag -v && coverage report" 

check-black:
	docker-compose run --rm app sh -c \
		"black src/rag && black tests/rag"

build:
	docker-compose build 

up:
	docker-compose up

down:
	docker-compose down

check-flake8:
	docker-compose run --rm app sh -c "flake8 src/rag tests" 
