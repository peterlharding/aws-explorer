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

count = 0

PICKLE_FILE = "stacks.pickle"

# -----------------------------------------------------------------------------

def load_pickled__data():
    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as f_in:
            data = pickle.load(f_in)

    else:
        data = {}
        save_data = True

    return data

# -----------------------------------------------------------------------------

def do_pickle(data):
    pass

# -----------------------------------------------------------------------------

client = boto3.client("cloudformation")

# -----------------------------------------------------------------------------

loop            = 0
next_token      = 1
total_cnt       = 0
not_deleted_cnt = 0
counts          = {}

while next_token:

    loop += 1

    if next_token == 1:
        results = client.list_stacks()
    else:
        results = client.list_stacks(NextToken=next_token)

    pp.pprint(results) 

    try:
        next_token = results["NextToken"]
    except KeyError as err:
        next_token = None

    response_metadata = results["ResponseMetadata"]
    stacks            = results["StackSummaries"]

    for stack in stacks:

        total_cnt += 1

        name       = stack["StackName"]
        status     = stack["StackStatus"]

        if not status in counts:
            counts[status]  = 1
        else:
            counts[status] += 1

        if status != "DELETE_COMPLETE":
            not_deleted_cnt += 1
            print(f"{name:100s}  {status}")


print()
print(f"Did {loop} call(s) to retrieve all data")
print()
print(f"Counted {total_cnt} total stacks")
print(f"Counted {not_deleted_cnt} undeleted stacks")
print()

keys = list(counts)

keylist = []

keylist.extend(iter(counts))

for key in keylist:
    print(f"    {key:40s}   {counts[key]:3d}")


# -----------------------------------------------------------------------------
#
#print(f"Count |{count}|")
#
#if save_function:
#    get_functions()
#
#print_functions()
#
#if save_functions:
#    with open(pickle_file, "wb+") as f_out:
#        pickle.dump(functions, f_out)
#
# -----------------------------------------------------------------------------

