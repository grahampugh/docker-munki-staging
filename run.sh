#!/bin/bash

python /etc/munki-staging/write_config.py
python /etc/munki-staging/munki-staging.py --config /etc/munki-staging/munki-staging-runtime.cfg
