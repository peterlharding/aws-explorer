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

REGION    = os.getenv("AWS_DEFAULT_REGION")
PROFILE   = sys.argv[1]
MAX_ITEMS = 50

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|")

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------

count = 0

PICKLE_FILE = "cf.pickle"

save_pickle = True

def load_pickled():
    if os.path.exists(PICKLE_FILE):
        with open(PICKLE_FILE, "rb") as f_in:
            data = pickle.load(f_in)

    else:
        data = {}
        save_pickle = True

    return data

# -----------------------------------------------------------------------------

def do_pickle(data):
    with open(PICKLE_FILE, "wb+") as f_out:
        pickle.dump(data, f_out)

# -----------------------------------------------------------------------------

client = boto3.client("cloudformation")

# -----------------------------------------------------------------------------

def print_stacks():

    idx = 0

    for name in sorted(stacks.keys(), key=str.casefold):

        idx += 1

        function = stacks[name]

        runtime = function["Runtime"]
        last    = function["LastModified"]
        role    = function["Role"][30:0]  # arn:aws:iam::111222333444:role/

        print(f"{idx:03}  {name:<70}  {role:<70}  {runtime:<12} {last}")

# -----------------------------------------------------------------------------

def get_block_of_stacks(marker=None):

    global count

    if not marker:
        results = client.list_stacks(MaxItems=MAX_ITEMS)
    else:
        results = client.list_stacks(Marker=marker, MaxItems=MAX_ITEMS)


    marker = results["NextMarker"]

    stacks = results["StackSummaries"]

    for stack in stacks:

        name = stack["StackName"]

        if not name in stacks.keys():
            stacks[name] = stack
            count += 1

        else:
            print(f"Found a duplicate - {name}")
            return None

    return marker

# -----------------------------------------------------------------------------

def get_stacks():

    marker = get_block_of_stacks()

    while marker != None:
        marker = get_block_of_stacks(marker)
 
# -----------------------------------------------------------------------------

next_token    = 1
total_cnt     = 9
deleted_cnt   = 0
loop          = 0

counts        = {}

result = client.delete_stack(StackName="cnp-fastapi-example-test", RetainResources=[])

"""

while next_token:

    loop += 1

    if next_token == 1:
        results = client.list_stacks()
    else:
        results = client.list_stacks(NextToken=next_token)


    # pp.pprint(results)

    try:
        next_token = results["NextToken"]
    except KeyError:
        next_token = None

    response_metadata = results["ResponseMetadata"]
    stacks            = results["StackSummaries"]

    for stack in stacks:

        total_cnt += 1

        name   = stack["Name"]
        status = stack["StackStatus"]

        if not status in counts:
            counts[status]  = 1
        else:
            counts[status] += 1

        if status == "DELETE COMPLETE":
            deleted_cnt += 1
            print(f"{name:100s}  {status}")
"""

"""
print(f"Count |{count}|")

if save_stacks:
    get_stacks()

print_stacks()

if save_stacks:
    with open(pickle_file, "wb+") as f_out:
        pickle.dump(stacks, f_out)
"""

# -----------------------------------------------------------------------------

