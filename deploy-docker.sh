#!/bin/bash
echo "... Updating python-mad-web: Restart the service"
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d --no-deps
