#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/arpitkaushik18/JSON_API.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/JSON_API

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/JSON_API

$VIRTUALENV_BASE_PATH/JSON_API/bin/pip install -r $PROJECT_BASE_PATH/JSON_API/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/JSON_API

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/JSON_API/deploy/supervisor_json_api.conf /etc/supervisor/conf.d/json_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart JSON_API

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/json_api/deploy/nginx_json_api.conf /etc/nginx/sites-available/json_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/json_api.conf /etc/nginx/sites-enabled/json_api.conf
systemctl restart nginx.service

echo "DONE! :)"
