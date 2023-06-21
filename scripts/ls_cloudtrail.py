#!/usr/bin/env python3
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
    print("Specify profile to use")
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

client = boto3.client("cloudtrail")

trails = client.describe_trails(includeShadowTrails=False)["trailList"]


for trail in trails:
    pp.pprint(trail)



