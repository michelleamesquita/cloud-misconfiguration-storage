#!/usr/bin/env bash

export AZURE_STORAGE_CONNECTION_STRING="$(terraform output -raw storage_account_primary_access_key)"

echo $AZURE_STORAGE_CONNECTION_STRING