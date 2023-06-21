#!/usr/bin.env python3
"""
  Standard setup block for boto3 based scripts
"""
# -----------------------------------------------------------------------------

import os
import sys
import json
import boto3
import pprint

# -----------------------------------------------------------------------------

if len(sys.argv) != 2:
    print("Specify profile to use"
    sys.exit(1)

# -----------------------------------------------------------------------------

REGION  = os.getenv("AWS_DEFAULT_REGION")
PROFILE = sys.argv[1]

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|")

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------


SLACK_APP_TOKEN = "/performiq/socket-mode-starter/slack-app-token"

client = boto3.client("ssm")

# -----------------------------------------------------------------------------

def get_param(path: str) -> str:

    response = client.get_parameter(Name=path, WithDecryption=True)
    param = response["Parameter"]

    value = param["Value"]

    return value

# -----------------------------------------------------------------------------

try:
    param_value = get_param(SLACK_APP_TOKEN)

    print(f"SLACK_APP_TOKEN |{SLACK_APP_TOKEN}|")

except Exception as ex:
    print(f"")

# -----------------------------------------------------------------------------

