#!/bin/bash
set -o errexit  # Exit the script with error if any of the commands fail
HERE=$(dirname ${BASH_SOURCE:-$0})
. $DRIVERS_TOOLS/.evergreen/csfle/azurekms/setup-secrets.sh
SUCCESS=false TEST_FLE_AZURE_AUTO=1 bash $HERE/scripts/setup-tests.sh
KEY_NAME="${AZUREKMS_KEYNAME}" \
    KEY_VAULT_ENDPOINT="${AZUREKMS_KEYVAULTENDPOINT}" \
    $HERE/just.sh test-eg
bash $HERE/scripts/teardown-tests.sh
