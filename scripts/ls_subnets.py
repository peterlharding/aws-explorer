#!/usr/bin/env python3
import boto3
import pprint

pp = pprint.PrettyPrinter(indent=4)

ec2 = boto3.client("ec2")

next_token = 1

total_cnt     = 0
undeleted_cnt = 0
loop          = False


counts = {}

results = ec2.describe_subnets()

# pp.pprint(results)

response_metadata = results["ResponseMetadata"]
subnets           = results["Subnets"]

print()
print(f" Number of Subnets |{len(subnets)}|")
print()
print("VPC ID                 Subnet ID                 AZ               CIDR Block          # Addr  Subnet Name        Associated Stack")

for subnet in subnets:

    info = {}

    # pp.pprint(subnet)

    vpc_id        = subnet["VpcId"]
    subnet_id     = subnet["SubnetId"]
    cidr_block    = subnet["CidrBlock"]
    az            = subnet["AvailabilityZone"]
    az_id         = subnet["AvailabilityZoneId"]

    if "AvailableIpAddressCount" in subnet:
        available_ip_count = subnet["AvailableIpAddressCount"]
    else:
        avaliable_ip_count = 0

    tags          = subnet["Tags"]
   

    for t in tags:

        key   = t["Key"]
        value = t["Value"]

        info[key] = value

        # pp.pprint(info)

    name          = info["Name"]

    if "aws:cloudformatoin:stack-name" in info:
        stack     = info["aws:cloudformatoin:stack-name"]
    else:
        stack     = None


    print(f"{vpc_id:21}  {subnet_id:24}  {az:15}  {cidr_block:20}  {available_ip_count}  {name:20}  {stack}")

    # pp.pprint(subnet)

print()
# results = clinet.list()


