build:
	docker-compose -f docker-compose.yml build

build-provision:
	docker-compose -f docker-compose.provision.yml build

setup:
	docker-compose -f docker-compose.yml up -d kong-db
	docker-compose -f docker-compose.yml up -d keycloak-db
	sleep 10
	docker-compose -f docker-compose.yml run --rm kong kong migrations bootstrap

provision:
	docker-compose -f docker-compose.provision.yml run --rm kong-provision

up:
	docker-compose -f docker-compose.yml up

down:
	docker-compose -f docker-compose.yml down --remove-orphans -v

logs:
	docker-compose -f docker-compose.yml logs --follow


run-kong-auth:
	docker-compose -f docker-compose.kong.auth.yml up -d