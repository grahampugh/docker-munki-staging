# docker-munki-trello

This Docker image runs pebble.it's [munki-trello](https://github.com/pebbleit/munki-trello) script. For more information about it's operation and on how to obtain the needed key and token, see the Readme for the origiginal repository.

# Settings

Several options are customizable using environment variables.

* ``DOCKER_TRELLO_KEY``: The API Key
* ``DOCKER_TRELLO_TOKEN``: This sets the name that appears in the title bar of the window. Defaults to ``Sal``.
* ``DOCKER_SAL_TZ``: The desired [timezone](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Defaults to ``Europe/London``.
* ``DOCKER_SAL_ADMINS``: The admin user's details. Defaults to ``Docker User, docker@localhost``.
* ``DOCKER_SAL_PLUGIN_ORDER``: The order plugins are displayed in. Defaults to ``Activity,Status,OperatingSystem,Uptime,Memory``.

If you require more advanced settings, for example if you want to hide certain plugins from certain Business Units or if you have a plugin that needs settings, you can override ``settings.py`` with your own. A good starting place can be found on this image's [Github repository](https://github.com/grahamgilbert/macadmins-sal/blob/master/settings.py).

```
  -v /usr/local/sal_data/settings/settings.py:/home/docker/sal/sal/settings.py
  ```

# Plugins

The plugins directory is exposed as a volume to the host, so you can add your own plugins using the ``-v`` option to link to ``/home/docker/sal/plugins`` in the container. 

```
  -v /usr/local/sal_data/plugins:/home/docker/sal/plugins
  ```

#Postgres container

Out of the box, Sal uses a SQLite database, however if you are running it in a production environment, it is recommended that you use a Postgres Database.
I have created a Postgres container that is set up ready to use with Sal - just tell it where you want to store your data, and pass it some environment variables for the database name, username and password.

* ``DB_NAME``
* ``DB_USER``
* ``DB_PASS``

```bash
$ docker pull grahamgilbert/postgres
$ docker run -d --name="postgres-sal" \
  -v /db:/var/lib/postgresql/data \
  -e DB_NAME=sal \
  -e DB_USER=admin \
  -e DB_PASS=password \
  --restart="always" \
  grahamgilbert/postgres
```

#Running the Sal Container

```bash
$ docker run -d --name="sal" \
  -p 80:8000 \
  --link postgres-sal:db \
  -e ADMIN_PASS=pass \
  -e DB_NAME=sal \
  -e DB_USER=admin \
  -e DB_PASS=password \
  --restart="always" \
  macadmins/sal
```

#TODO

* Add support for SQLite and MySQL
