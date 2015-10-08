#!/usr/bin/python

import os
import ConfigParser
import sys

def fail(message):
    print message
    sys.exit(1)

config_path = '/etc/munki-staging/munki-staging.cfg'

main = {}
munki_repo_default = {}
munki_catalog_development = {}
munki_catalog_testing = {}
munki_catalog_production = {}
rssfeeds = {}
if os.environ['DOCKER_STAGING_KEY']=='null':
    fail("Trello API Key not set")
else:
    main['key'] = os.environ['DOCKER_STAGING_KEY']

if os.environ['DOCKER_STAGING_TOKEN']=='null':
    fail("Trello API Token not set")
else:
    main['token'] = os.environ['DOCKER_STAGING_TOKEN']

if os.environ['DOCKER_STAGING_BOARDID']=='null':
    fail("Trello Board ID not set")
else:
    main['boardid'] = os.environ['DOCKER_STAGING_BOARDID']

main['repo_path'] = os.environ['DOCKER_STAGING_MUNKI_PATH']
main['date_format'] = os.environ['DOCKER_STAGING_DATE_FORMAT']
main['makecatalogs'] = os.environ['DOCKER_STAGING_MAKECATALOGS']

munki_repo_default_name = "munki_repo_" + os.environ['DOCKER_STAGING_DEFAULT_REPO']
munki_repo_default['repo_path'] = os.environ['DOCKER_STAGING_MUNKI_PATH']

munki_catalog_development['list'] = os.environ['DOCKER_STAGING_DEV_LIST']
munki_catalog_development['munki_repo'] = os.environ['DOCKER_STAGING_DEFAULT_REPO']
munki_catalog_development['catalog'] = os.environ['DOCKER_DEV_CATALOG']
munki_catalog_development['to_list'] = os.environ['DOCKER_STAGING_TO_DEV_LIST']
munki_catalog_development['autostage'] = os.environ['DOCKER_STAGING_DEV_AUTOSTAGE']
munki_catalog_development['stage_days'] = os.environ['DOCKER_STAGING_DEV_STAGE_DAYS']
munki_catalog_development['stage_to'] = os.environ['DOCKER_STAGING_DEV_STAGE_TO']

munki_catalog_testing['list'] = os.environ['DOCKER_STAGING_TEST_LIST']
munki_catalog_testing['munki_repo'] = os.environ['DOCKER_STAGING_DEFAULT_REPO']
munki_catalog_testing['catalog'] = os.environ['DOCKER_TEST_CATALOG']
munki_catalog_testing['to_list'] = os.environ['DOCKER_STAGING_TO_TEST_LIST']
munki_catalog_testing['autostage'] = os.environ['DOCKER_STAGING_TEST_AUTOSTAGE']
munki_catalog_testing['stage_days'] = os.environ['DOCKER_STAGING_TEST_STAGE_DAYS']
munki_catalog_testing['stage_to'] = os.environ['DOCKER_STAGING_TEST_STAGE_TO']

if os.environ['DOCKER_STAGING_PRODUCTION_LIST'] != 'null':
    munki_catalog_production['list'] = os.environ['DOCKER_STAGING_PRODUCTION_LIST']
munki_catalog_production['munki_repo'] = os.environ['DOCKER_STAGING_DEFAULT_REPO']
munki_catalog_production['catalog'] = os.environ['DOCKER_PROD_CATALOG']
munki_catalog_production['to_list'] = os.environ['DOCKER_STAGING_TO_PROD_LIST']
munki_catalog_production['suffix'] = os.environ['DOCKER_STAGING_SUFFIX']

if os.environ['DOCKER_STAGING_PRODUCTION_LIST'] != 'null':
    rssfeeds['rssdir'] = os.environ['DOCKER_STAGING_RSSDIR']
    rssfeeds['rss_link_template'] = os.environ['DOCKER_STAGING_RSS_LINK_TEMPLATE']
    rssfeeds['guid_link_template'] = os.environ['DOCKER_STAGING_RSS_GUID_LINK_TEMPLATE']
    rssfeeds['catalog_link_template'] = os.environ['DOCKER_STAGING_RSS_CATALOG_LINK_TEMPLATE']
    rssfeeds['description_template'] = os.environ['DOCKER_STAGING_RSS_DESCRIPTION_TEMPLATE']
    rssfeeds['icon_url_template'] = os.environ['DOCKER_STAGING_RSS_ICON_URL_TEMPLATE']

parser = ConfigParser.ConfigParser()
parser.add_section('main')
for key in main.keys():
    parser.set('main', key, main[key])

parser.add_section(munki_repo_default_name)
for key in munki_repo_default.keys():
    parser.set(munki_repo_default_name, key, munki_repo_default[key])

parser.add_section('munki_catalog_development')
for key in munki_catalog_development.keys():
    parser.set('munki_catalog_development', key, munki_catalog_development[key])

parser.add_section('munki_catalog_testing')
for key in munki_catalog_testing.keys():
    parser.set('munki_catalog_testing', key, munki_catalog_testing[key])

parser.add_section('munki_catalog_production')
for key in munki_catalog_production.keys():
    parser.set('munki_catalog_production', key, munki_catalog_production[key])

if os.environ['DOCKER_STAGING_PRODUCTION_LIST'] != 'null':
    parser.add_section('rssfeeds')
    for key in rssfeeds.keys():
        parser.set('rssfeeds', key, rssfeeds[key])

with open(config_path, 'w') as f:
    parser.write(f)
