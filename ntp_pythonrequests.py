from intersight_auth import IntersightAuth
from requests import Session
import urllib.parse
import os


session = Session()
api_key_id = os.environ["INTERSIGHT_API_KEY_ID"]
api_key = os.environ["INTERSIGHT_API_PRIVATE_KEY"]
session.auth = IntersightAuth(api_key_id=api_key_id, secret_key_string=api_key)

filter = urllib.parse.quote("Name eq 'CLUS'")
org = session.get(
    f"https://intersight.com/api/v1/organization/Organizations?$filter={filter}"
).json()["Results"][0]

theNTPPolicy = {
    "Name": "python_requests",
    "Description": "This is an NTP policy created with Python SDK",
    "Organization": {"ObjectType": org["ObjectType"], "Moid": org["Moid"]},
    "Enabled": True,
    "NtpServers": ["1.1.1.1", "2.2.2.2"],
    "Tags": [
        {"Key": "CLUS2023", "Value": "Devnet-1061"},
        {"Key": "Language", "Value": "Python Requests"},
    ],
    "Timezone": "America/Phoenix",
}
ntp_response = session.post(
    "https://intersight.com/api/v1/ntp/Policies", json=theNTPPolicy
)


# ############
# ############
# # Here we have an alternate example that we're not going to actually use
# # We can just grab the body from the browser and we drop it into a raw string
# # And we can put that right back into Intersight
# ############
#
# # We're using an `r` or RAW string type here and using exactly what we observed.
# theNTPPolicy_string = r'{"Organization":{"ObjectType":"organization.Organization","Moid":"64079cb76972652d336afc9f"},"Name":"requests","Tags":[{"Key":"CLUS2023","Value":"Devnet-1061"},{"Key":"Language","Value":"Python Requests"}],"Description":"This is a description","Enabled":true,"NtpServers":["11.1.1.1","2.2.2.2"],"Timezone":"America/Phoenix"}'
#
# # We then post that string as the body
# ntp_response = session.post(
#     "https://intersight.com/api/v1/ntp/Policies", json=theNTPPolicy_string
# )
# ############
# ############
