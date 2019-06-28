#!/bin/sh
# If the secrets file exists, read it in.
if [ -f secrets.sh ]; then
  . secrets.sh
fi

# Start Gunicorn app server
pipenv run gunicorn thistle.wsgi:application \
               --bind 0.0.0.0:8005 \
               --workers 5

# Now run the main container CMD, replacing this script.
exec "$@"