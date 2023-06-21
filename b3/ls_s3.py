#!/usr/bin/env python3

import boto3
import pprint

pp = pprint.PrettyPrinter(indent=4)

client = boto3.resource('s3')

all = client.buckets.all()

for bucket in all:
    pp.pprint(bucket)


