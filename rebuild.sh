#!/bin/bash

set -ex

docker-compose -f deployment/docker-compose.yaml build --no-cache