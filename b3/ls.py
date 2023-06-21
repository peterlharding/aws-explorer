#!/usr/bin/env python3

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name='piq')

client = boto3.client('s3')

# results = cleint.scan_provisioned_products()

all = client.list_buckets()

for bucket in all:
    pp.pprint(bucket)


