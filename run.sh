#!/bin/bash

python /write_config.py
python /munki-trello/munki-trello.py --suffix "$DOCKER_TRELLO_SUFFIX" --makecatalogs /munki-tools/code/client/makecatalogs
