# docker-munki-trello

This Docker image runs the [munki-trello](https://github.com/grahamgilbert/munki-trello) script. For more information about it's operation and on how to obtain the needed key and token, see the Readme for the original repository.

# Settings

Several options are customizable using environment variables.

* ``DOCKER_TRELLO_KEY``: The API Key
* ``DOCKER_TRELLO_TOKEN``: The Trello Application Token.
* ``DOCKER_TRELLO_BOARDID``: The Trello Board ID.
* ``DOCKER_TRELLO_TO_DEV_LIST``: The name of the 'To Development' list. Defaults to ``To Development``.
* ``DOCKER_TRELLO_DEV_LIST``: The name of the 'Development' list. Defaults to ``Development``.
* ``DOCKER_TRELLO_TO_TEST_LIST``: The name of the 'To Testing' list. Defaults to ``To Testing``.
* ``DOCKER_TRELLO_TEST_LIST``: The name of the 'Testing' list. Defaults to ``Testing``.
* ``DOCKER_TRELLO_TO_PROD_LIST``: The name of the 'To Production' list. Defaults to ``To Production``.
* ``DOCKER_TRELLO_MUNKI_PATH``: The path in the container to the Munki repository. Defaults to ``/munki_repo``.
* ``DOCKER_TRELLO_SUFFIX``:  Suffix for newly created 'Production' lists. Defaults to ``Production``.
* ``DOCKER_DEV_CATALOG``: Development Munki catalog. Defaults to ``development``.
* ``DOCKER_TEST_CATALOG`` Testing Munki catalog. Defaults to ``testing``.
* ``DOCKER_PROD_CATALOG``: Production Munki catalo. Defaults to ``production``.
* ``DOCKER_TRELLO_DATE_FORMAT``: Date format for Production lists. Defaults to ``%d/%m/%y``.
* ``DOCKER_TRELLO_AUTO_STAGE_TO_TEST``: Enable auto staging to test. Defaults to ``False``.
* ``DOCKER_TRELLO_AUTO_STAGE_TO_PROD``: Enable auto staging to production. Defaults to ``False``.
* ``DOCKER_TRELLO_DEV_STAGE_DAYS``: Days until autostaging from Development to Test. Defaults to ``0``.
* ``DOCKER_TRELLO_TEST_STAGE_DAYS``: Days until autostaging from Testing to Production. Defaults to ``0``.
* ``DOCKER_TRELLO_PRODUCTION_LIST`` Name of the Production list. Ignored if ``DOCKER_TRELLO_SUFFIX`` isn't set to an empty string.

DOCKER_TRELLO_KEY="null" \
    DOCKER_TRELLO_TOKEN="null" \
    DOCKER_TRELLO_BOARDID="null" \
    DOCKER_TRELLO_TO_DEV_LIST="To Development" \
    DOCKER_TRELLO_DEV_LIST="Development" \
    DOCKER_TRELLO_TO_TEST_LIST="To Testing" \
    DOCKER_TRELLO_TEST_LIST="Testing" \
    DOCKER_TRELLO_TO_PROD_LIST="To Production" \
    DOCKER_TRELLO_MUNKI_PATH="/munki_repo" \
    DOCKER_TRELLO_SUFFIX="Production" \
    DOCKER_DEV_CATALOG="development" \
    DOCKER_TEST_CATALOG="testing" \
    DOCKER_PROD_CATALOG="production" \
    DOCKER_TRELLO_DATE_FORMAT="%d/%m/%y" \
    DOCKER_TRELLO_AUTO_STAGE_TO_TEST="False" \
    DOCKER_TRELLO_AUTO_STAGE_TO_PROD="False" \
    DOCKER_TRELLO_DEV_STAGE_DAYS="0" \
    DOCKER_TRELLO_TEST_STAGE_DAYS="0" \
    DOCKER_TRELLO_PRODUCTION_LIST="null"


#Running the container

It's recommended to run this container using the ``--rm`` option so the container is destroyed after the script has run.

```bash
$ docker pull pebbleit/munki-trello
$ docker run --rm \
  -v /var/www/munki:/munki_repo \
  -e DOCKER_TRELLO_KEY=yourapikey \
  -e DOCKER_TRELLO_TOKEN=yourtoken \
  -e DOCKER_TRELLO_BOARDID=abc123 \
  pebbleit/munki-trello
```
