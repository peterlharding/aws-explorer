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

if len(sys.argv) != 3:
    print("Specify profile and role to use")
    sys.exit(1)

# -----------------------------------------------------------------------------

REGION    = os.getenv("AWS_DEFAULT_REGION")
PROFILE   = sys.argv[1]
ROLE_NAME = sys.argv[2]

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|  ROLE_NAME |{ROLE_NAME}|")

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------

count = 0

PICKLE_FILE = "roles.pickle"

# -----------------------------------------------------------------------------

def unpickle_data():
    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as f_in:
            data = pickle.load(f_in)

    else:
        data = {}
        save_data = True

    return data

# -----------------------------------------------------------------------------

def do_pickle(data):
    with open(PICKLE_FILE, "wb+") as f_out:
        pickle.dump(data, f_out)

# -----------------------------------------------------------------------------

client = boto3.client("iam")

# -----------------------------------------------------------------------------

def print_data(data):

    idx = 0

    for name in sorted(data.keys(), key=str.casefold):

        idx += 1

        function = data[name]

        runtime = function["Runtime"]
        last    = function["LastModified"]
        role    = function["Role"][30:0]  # arn:aws:iam::111222333444:role/

        print(f"{idx:03}  {name:<70}  {role:<70}  {runtime:<12} {last}")

# -----------------------------------------------------------------------------

def get_block_of_records(marker=None):

    global count

    if not marker:
        results = lambdas.list_functions(FunctionVersion="ALL", MaxItems=50)
    else:
        results = lambdas.list_functions(Marker=marker, FunctionVersion="ALL", MaxItems=50)


    marker = results["NextMarker"]

    funcs  = results["Functions"]

    for func in funcs:
        name = func["FunctionName"]

        if not name in functions.keys():
            functions[name] = func
            count += 1

        else:
            print(f"Found a duplicate - {name}")
            return None

    return marker

# -----------------------------------------------------------------------------

def get_records():

    marker = get_block_of_records()

    while marker != None:
        marker = get_block_of_records(marker)
 
# -----------------------------------------------------------------------------

results = client.get_role(RoleName=ROLE_NAME)

metadata  = results["ResponseMetadata"]
role_json = results["Role"]

print()
print("Role Details")
print("============")
print()
pp.pprint(role_json)
print()
#print(f"Count |{count}|")

#if save_function:
#    get_functions()

#print_functions()

#if save_data:
#     do_pickle(roles)

# -----------------------------------------------------------------------------

