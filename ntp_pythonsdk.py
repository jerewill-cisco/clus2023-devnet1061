import re
from pprint import pprint
import os

import intersight
from intersight.api import ntp_api, organization_api
from intersight.model.ntp_policy import NtpPolicy
from intersight.model.organization_organization_relationship import (
    OrganizationOrganizationRelationship,
)


# This function basically sorts out which kind of API key you generated from Intersight and
# does the setup of for the SDK ApiClient.
def get_api_client(api_secret_file, endpoint="https://intersight.com"):
    with open(api_secret_file, "r") as f:
        api_key = f.read()
        api_key_id = os.environ["INTERSIGHT_API_KEY_ID"]

    if re.search("BEGIN RSA PRIVATE KEY", api_key):
        # API Key v2 format
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15
        signing_scheme = intersight.signing.SCHEME_RSA_SHA256
        hash_algorithm = intersight.signing.HASH_SHA256

    elif re.search("BEGIN EC PRIVATE KEY", api_key):
        # API Key v3 format
        signing_algorithm = (
            intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
        )
        signing_scheme = intersight.signing.SCHEME_HS2019
        hash_algorithm = intersight.signing.HASH_SHA256

    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_path=api_secret_file,
            signing_scheme=signing_scheme,
            signing_algorithm=signing_algorithm,
            hash_algorithm=hash_algorithm,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ],
        ),
    )

    # if you want to turn off certificate verification
    # configuration.verify_ssl = False

    return intersight.ApiClient(configuration)


api_client = get_api_client("key.pem")
org_api_instance = organization_api.OrganizationApi(api_client)
ntp_api_instance = ntp_api.NtpApi(api_client)

org = org_api_instance.get_organization_organization_list(
    filter="Name eq 'CLUS'"
).results[0]

theOrgReference = OrganizationOrganizationRelationship(
    class_id="mo.MoRef",
    object_type=org.object_type,
    moid=org.moid,
)

theNtpPolicy = NtpPolicy()
theNtpPolicy.name = "python_sdk"
theNtpPolicy.description = "This is an NTP policy created with Python SDK"
theNtpPolicy.organization = theOrgReference
theNtpPolicy.enabled = True
theNtpPolicy.ntp_servers = ["1.1.1.1", "2.2.2.2"]
theNtpPolicy.tags = [
    dict(key="CLUS2023", value="Devnet-1061"),
    dict(key="Language", value="Python SDK"),
]
theNtpPolicy.timezone = "America/Phoenix"

ntp_response = ntp_api_instance.create_ntp_policy(theNtpPolicy)
