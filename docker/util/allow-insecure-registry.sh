#!/bin/bash

#read -p "Docker registry host:port: " -r
#DOCKER_REGISTRY=${REPLY}

source ../setenv.sh
if [ -e ../setenv_local.sh ]
then
    source ../setenv_local.sh
fi

echo "{ \"insecure-registries\" : [\"${DOCKER_REGISTRY}\"] }" | sudo tee /etc/docker/daemon.json