#!/bin/bash
export INTERSIGHT_API_KEY_ID=$(cat key.id)
export INTERSIGHT_API_PRIVATE_KEY=$(cat key.pem)
export TF_VAR_INTERSIGHT_API_KEY_ID=$(cat key.id)
export TF_VAR_INTERSIGHT_API_PRIVATE_KEY=$(cat key.pem)
