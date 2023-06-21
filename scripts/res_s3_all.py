#!/usr/bin/env python3

import boto3

session = boto3.session.Session(profile_name='piq')

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)



