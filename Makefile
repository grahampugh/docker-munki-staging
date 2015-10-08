MUNKI_REPO=/Users/glgrp/src/munki_repo
KEY:=
BOARDID:=
TOKEN:=
DOCKER_USER=grahampugh
NAME:=munki-staging
DOCKER_RUN_COMMON=--name="$(NAME)" -v ${MUNKI_REPO}:/munki_repo -e DOCKER_STAGING_KEY=${KEY} -e DOCKER_STAGING_BOARDID=${BOARDID} -e DOCKER_STAGING_TOKEN=${TOKEN} ${DOCKER_USER}/${NAME}


all: build

build:
	docker build -t="${DOCKER_USER}/${NAME}" .

build-nocache:
	docker build --no-cache=true -t="${DOCKER_USER}/${NAME}" .

run:
	docker run --rm ${DOCKER_RUN_COMMON}

interactive:
	docker run -i ${DOCKER_RUN_COMMON}

bash:
	docker run -t -i ${DOCKER_RUN_COMMON} /bin/bash

clean:
	docker stop $(NAME)
	docker rm $(NAME)

rmi:
	docker rmi ${DOCKER_USER}/${NAME}