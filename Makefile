NAME = cinefast
COMPOSE = docker-compose.yml

all: build up

cert:
	@mkdir -p Nginx/cert
	@openssl req -x509 -newkey rsa:2048 -keyout Nginx/cert/server.key -out Nginx/cert/server.crt -days 365 -nodes -subj "/C=FR/ST=FRANCE/L=ANGOULEME/CN=GMARRE"

volume:
	# @mkdir -p data/postgres
	@mkdir -p data/django

build: volume cert
	@docker compose -p $(NAME) -f $(COMPOSE) build

up: 
	@docker compose -p $(NAME) -f $(COMPOSE) up

down:
	@docker compose -p $(NAME) -f $(COMPOSE) down --volumes

clean: down
	rm -rf data/postgres
	rm -rf data/django
	rm -rf nginx/cert

re: clean all

back: clean volume
	@docker compose -p $(NAME) -f $(COMPOSE_BACK) build
	@docker compose -p $(NAME) -f $(COMPOSE_BACK) up

.PHONY: volume all build up down clean re back
