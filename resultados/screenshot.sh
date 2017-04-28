#!/bin/bash

INITIAL_SLEEP=5

#BASENAME=$(mktemp /tmp/screencast-XXXX)
BASENAME=screen

MAX=0

INTERVAL=0.5

I=$INITIAL_SLEEP

while [ $I != 0 ]; do
  echo -n $I...
#  sleep 1
  I=$(( $I - 1 ))
done
echo "Starting now"

I=0

while [ 1 ]; do
  FILENAME=$BASENAME/R$I.png
  echo -n "Saving ${FILENAME}"
  if import -window root ${FILENAME}; then
    echo "done."
  else
    echo "failed."
  fi

  I=$(( $I + 1 ))

  if [ $MAX -gt 0 -a $MAX -eq $I ]; then
    break
  fi
  sleep $INTERVAL

done
