#!/usr/bin.env python3
#
#
# -----------------------------------------------------------------------------
"""
  Using boto3.client() methods
"""
# -----------------------------------------------------------------------------

import os
import sys
import json
import boto3
import pprint
import pickle

# -----------------------------------------------------------------------------

if len(sys.argv) == 2:
    PROFILE = sys.argv[1]
else:
    PROFILE = "default"

REGION  = os.getenv("AWS_DEFAULT_REGION")

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|")

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)


# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------

iam_client    = boto3.client("iam")
lambda_client = boto3.client("lambda")

name = sys.argv[1]

results = lambda_client.get_function_configuration(FunctionName=name)

# lambda = results["Metadata"]

role = results["Role"]

offset = role.rfind("/")

print(offset)

role_name = role[offset+1:]

print(f"Role |{role}|  Name |{role_name}|")

print()
print("Lambda Details")
print("==============")
print()
pp.pprint(results)

role_details = role_client.get_role(RoleName=role_name)

metadata = role_details["ResponseMetadata"]
role_json = role_details["Role"]



print()
print("Role Details")
print("============")
print()
pp.pprint(role_json)
print()


# =============================================================================
#     Date       Who       Description
# -----------------------------------------------------------------------------
#  2023-06-21    plh       Initial setup#
# -----------------------------------------------------------------------------

