#!/usr/bin/env bash

terraform init
terraform apply --auto-approve

chmod +x ./set_primary_key.sh
. ./set_primary_key.sh

pip3 install -r requirements.txt

python3 app.py