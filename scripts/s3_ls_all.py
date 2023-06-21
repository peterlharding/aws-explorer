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

if len(sys.argv) == 2:
    PROFILE = sys.argv[1]
else:
    PROFILE = "default"

REGION  = os.getenv("AWS_DEFAULT_REGION")
AREA    = "s3"

count   = 0

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|  AREA |{AREA}|") 

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

# -----------------------------------------------------------------------------
# ...
# -----------------------------------------------------------------------------

PICKLE_FILE = f"{AREA}.pickle"

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

# =============================================================================

client = boto3.client(AREA)

# -----------------------------------------------------------------------------

def print_data():

    idx = 0

    for name in sorted(data.keys(), key=str.casefold):

        idx += 1

        obj = data[name]

        runtime = data["Runtime"]
        last    = data["LastModified"]
        role    = data["Role"][30:0]  # arn:aws:iam::111222333444:role/

        print(f"{idx:03}  {name:<70}  {role:<70}  {runtime:<12} {last}")

# -----------------------------------------------------------------------------

def get_block_of_records(records={}, marker=None):

    global count

    if not marker:
        results = client.list_functions(FunctionVersion="ALL", MaxItems=50)
    else:
        results = client.list_functions(Marker=marker, FunctionVersion="ALL", MaxItems=50)

    marker = results["NextMarker"]
    funcs  = results["Functions"]

    for func in funcs:
        name = func["FunctionName"]

        if not name in functions.keys():
            records[name] = func
            count += 1

        else:
            raise Exception(f"Found a duplicate - {name}")

    return records, marker

# -----------------------------------------------------------------------------

def get_data(records):

    records, marker = get_block_of_records(records)

    while marker != None:
        records, marker = get_block_of_records(records, marker)
 
# -----------------------------------------------------------------------------

# print(f"Read count |{count}| records")

# records = unpickle_data()

# if save_data:
#     get_data(records)

# print_data()

# if save_data:
#     do_pickle(records)

s3 = boto3.resource('s3')

buckets = s3.buckets.all()

for bucket in buckets:
    pp.pprint(bucket)


# -----------------------------------------------------------------------------

