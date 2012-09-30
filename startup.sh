#!/bin/bash
  set -e
  LOGFILE=/var/log/gunicorn/macnamer.log
  LOGDIR=$(dirname $LOGFILE)
  NUM_WORKERS=3
  # user/group to run as
  USER=www-data
  GROUP=www-data
  cd /srv/macnamer
  source /home/graham/.virtualenvs/macnamer/bin/activate
  test -d $LOGDIR || mkdir -p $LOGDIR
  exec /home/graham/.virtualenvs/macnamer/bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE --bind 127.0.0.1:8001
