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

count          = 0
save_functions = False

pickle_file = "lambda.pickle"

if os.path.exists(pickle_file):
    with open(pickle_file, "rb") as f_in:
        functions = pickle.load(f_in)

else:
    functions = {}
    save_functions = True

# -----------------------------------------------------------------------------

lambdas = boto3.client("lambda")

# -----------------------------------------------------------------------------

def print_functions():

    idx = 0

    for name in sorted(functions.keys(), key=str.casefold):

        idx += 1

        function = functions[name]

        runtime = function["Runtime"]
        last    = function["LastModified"]
        role    = function["Role"][30:0]  # arn:aws:iam::111222333444:role/

        print(f"{idx:03}  {name:<70}  {role:<70}  {runtime:<12} {last}")

# -----------------------------------------------------------------------------

def get_block_of_functions(marker=None):

    global count

    if not marker:
        results = lambdas.list_functions(FunctionVersion="ALL", MaxItems=50)
    else:
        results = lambdas.list_functions(Marker=marker, FunctionVersion="ALL", MaxItems=50)


    try:
        marker = results["NextMarker"]
    except:
        marker = None

    funcs = results["Functions"]

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

def get_functions():

    marker = get_block_of_functions()

    while marker != None:
        marker = get_block_of_functions(marker)
 
# -----------------------------------------------------------------------------

print(f"Count |{count}|")

if save_functions:
    get_functions()

print_functions()

if save_functions:
    with open(pickle_file, "wb+") as f_out:
        pickle.dump(functions, f_out)

# -----------------------------------------------------------------------------

