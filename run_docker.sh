#!/bin/sh

clear;

docker build -f Dockerfile . -t task_3_app && \
  docker-compose -f docker-compose.yml -p 'task_3_app_network' up --remove-orphans
