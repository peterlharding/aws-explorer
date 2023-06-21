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
import pickle

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

iam = boto3.client("iam")

count = 0

refresh_data = 0

pickle_file = "iam_role.pickle"

if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as f_in:
        data = pickle.load(f_in)
else:
    data = {}
    refresh_data = True

# -----------------------------------------------------------------------------

def print_roles():
    idx = 0

    for name in sorted(data.keys(), key=str.casefold):

        idx += 1

        # runtime = data["runtime"]
        # last    = data["lastModified"]
        # role    = data["role"][30:0]  # arn:aws:iam::111222333444:role/...

        print(f"{idx:03}  {name:<70}")

# -----------------------------------------------------------------------------

def get_block_of_roles(marker=None):

    global count

    if not marker:
        results = iam.list_roles(MaxItems=50)

    else:
        results = iam.list_roles(Marker=marker, MaxItems=100)

    pp.pprint(results)

    roles = results["Roles"]

    print(len(roles))

    try:
        marker = results["marker"]

    except:
        marker = None


    print(f"Marker |{marker}|")
    print(f"Scooped up {len(roles)} roles...")

    for role in roles:
        name = role["RoleName"]

        if not name in data.keys():
            data[name] = role
            count += 1
        else:
            print(f"Found a duplicate - {name}")
            return None

    return marker

# -----------------------------------------------------------------------------

def get_roles():

    marker = get_block_of_roles()

    while marker != None:
        marker = get_block_of_roles(marker)


# -----------------------------------------------------------------------------

print(f"Count |{count}|")

if refresh_data:
    get_roles()

print_roles()

if refresh_data:
    with open(pickle_file, "wb+") as f_out:
        pickle.dump(data, f_out)



# -----------------------------------------------------------------------------


