#!/usr/bin/python

import os
import ConfigParser
import sys

def fail(message):
    print message
    sys.exit(1)

config_path = '/munki-trello/munki-trello.cfg'

main = {}
development = {}
testing = {}
production = {}
if os.environ['DOCKER_TRELLO_KEY']=='null':
    fail("Trello API Key not set")
else:
    main['key'] = os.environ['DOCKER_TRELLO_KEY']

if os.environ['DOCKER_TRELLO_TOKEN']=='null':
    fail("Trello API Token not set")
else:
    main['token'] = os.environ['DOCKER_TRELLO_TOKEN']

if os.environ['DOCKER_TRELLO_BOARDID']=='null':
    fail("Trello Board ID not set")
else:
    main['boardid'] = os.environ['DOCKER_TRELLO_BOARDID']

main['repo_path'] = os.environ['DOCKER_TRELLO_MUNKI_PATH']
main['date_format'] = os.environ['DOCKER_TRELLO_DATE_FORMAT']
development['list'] = os.environ['DOCKER_TRELLO_DEV_LIST']
development['catalog'] = os.environ['DOCKER_DEV_CATALOG']
development['to_list'] = os.environ['DOCKER_TRELLO_TO_DEV_LIST']
development['stage_days'] = os.environ['DOCKER_TRELLO_DEV_STAGE_DAYS']
testing['list'] = os.environ['DOCKER_TRELLO_TEST_LIST']
testing['catalog'] = os.environ['DOCKER_TEST_CATALOG']
testing['to_list'] = os.environ['DOCKER_TRELLO_TO_TEST_LIST']
testing['stage_days'] = os.environ['DOCKER_TRELLO_DEV_STAGE_DAYS']
testing['autostage'] = os.environ['DOCKER_TRELLO_AUTO_STAGE_TO_TEST']

if os.environ['DOCKER_TRELLO_PRODUCTION_LIST'] != 'null':
    production['list'] = os.environ['DOCKER_TRELLO_PRODUCTION_LIST']
production['catalog'] = os.environ['DOCKER_TRELLO_SUFFIX']
production['to_list'] = os.environ['DOCKER_TRELLO_TO_PROD_LIST']
production['stage_days'] = os.environ['DOCKER_TRELLO_TEST_STAGE_DAYS']
production['autostage'] = os.environ['DOCKER_TRELLO_AUTO_STAGE_TO_PROD']
production['suffix'] = os.environ['DOCKER_TRELLO_SUFFIX']

parser = ConfigParser.ConfigParser()
parser.add_section('main')
for key in main.keys():
    parser.set('main', key, main[key])

parser.add_section('development')
for key in development.keys():
    parser.set('development', key, development[key])

parser.add_section('testing')
for key in testing.keys():
    parser.set('testing', key, testing[key])

parser.add_section('production')
for key in production.keys():
    parser.set('production', key, production[key])

with open(config_path, 'w') as f:
    parser.write(f)
