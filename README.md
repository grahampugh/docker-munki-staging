# docker-munki-staging

This Docker image runs the [munki-staging](https://github.com/ox-it/munki-staging) script. For more information about it's operation and on how to obtain the needed key and token, see the Readme for the original repository.

# Settings

Several options are customizable using environment variables. These are set as follows in the `Dockerfile` as downloaded. For more details, see the notes in `munki-staging.cfg`, but they're all self-explanatory, except to note that `DOCKER_STAGING_MUNKI_PATH` refers to the path in the container, not on your host computer:

```
    DOCKER_STAGING_KEY="null" \
    DOCKER_STAGING_TOKEN="null" \
    DOCKER_STAGING_BOARDID="null" \
    DOCKER_DEV_CATALOG="development" \
    DOCKER_STAGING_TO_DEV_LIST="To Development" \
    DOCKER_STAGING_DEV_LIST="Development" \
    DOCKER_STAGING_DEV_AUTOSTAGE="0" \
    DOCKER_STAGING_DEV_STAGE_DAYS="0" \
    DOCKER_STAGING_DEV_STAGE_TO="Testing" \
    DOCKER_TEST_CATALOG="testing" \
    DOCKER_STAGING_TO_TEST_LIST="To Testing" \
    DOCKER_STAGING_TEST_LIST="Testing" \
    DOCKER_STAGING_TEST_AUTOSTAGE="0" \
    DOCKER_STAGING_TEST_STAGE_DAYS="0" \
    DOCKER_STAGING_TEST_STAGE_TO="Production" \
    DOCKER_PROD_CATALOG="production" \
    DOCKER_STAGING_TO_PROD_LIST="To Production" \
    DOCKER_STAGING_SUFFIX="Production" \
    DOCKER_STAGING_MUNKI_PATH="/munki_repo" \
    DOCKER_STAGING_DEFAULT_REPO="default" \
    DOCKER_STAGING_MAKECATALOGS="/munki-tools/code/client/makecatalogs" \
    DOCKER_STAGING_DATE_FORMAT="%d/%m/%y" \
    DOCKER_STAGING_PRODUCTION_LIST="Production" \
    DOCKER_STAGING_RSSDIR="null" \
    DOCKER_STAGING_RSS_LINK_TEMPLATE="null" \
    DOCKER_STAGING_RSS_GUID_LINK_TEMPLATE="null" \
    DOCKER_STAGING_RSS_CATALOG_LINK_TEMPLATE="null" \
    DOCKER_STAGING_RSS_DESCRIPTION_TEMPLATE="null" \
    DOCKER_STAGING_RSS_ICON_URL_TEMPLATE="null"
```
# Configuring your Trello settings

```bash
$ cd ~/src/  # change to wherever you store your git clones
$ git clone https://github.com/grahampugh/docker-munki-staging.git
$ cd docker-munki-staging/
```

  * Amend settings in the `Dockerfile` as required.
  * Add your Trello API Key, Board ID and Token to the `Makefile`, and set your host Munki Repo path. This expects that you are volume linking your Munki repo from a directory on your host to the docker container. If you are running a separate Munki-Repo data container, you'll need to edit the `make run` command or construct your own docker run command (see below).
  * If you wish, you can edit `munki-staging.cfg` to add further customisations such as an additional Munki Repo, or scheduling, as these keys aren't built into the Dockerfile. Any settings you set in `munki-staging.cfg` will supercede any set in the `Dockerfile`.

# Running the container

```bash
$ make build
$ make run
```

It's recommended to run this container using the ``--rm`` option so the container is destroyed after the script has run. The command `make run` has been pre-defined to run the correct `docker run` command with the Trello IDs and volume link to your Munki Repo.