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

spacer = 120 * "-"


boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------

client = boto3.client("autoscaling")


results = client.describe_auto_scaling_groups()

metadata = results["ResponseMetadata"]

pp.pprint(metadata)

print()
print(spacer)

asg = results["AutoScalingGroups"]

cnt = 0


for block in asg:
    cnt += 1
    name = block["AutoScalingGroupName"]
    instances = block["Instances"]
    no_instances = len(instances)

    print(f"Name {name:>30} -> No of instances {no_instances}")
    print()
    pp.print(block)
    print(spacer)
    print()


print()
print(f"Found {cnt} ASG in {PROFILE}")
print()



