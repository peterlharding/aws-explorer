#!/usr/bin.env python3
"""
  Standard setup block for boto3 based scripts
"""

import os
import sys
import json
import boto3
import pprint

if len(sys.argv) != 2:
    print("Specify profile to use"
    sys.exit(1)


REGION  = os.getenv("AWS_DEFAULT_REGION")
PROFILE = sys.argv[1]

print(f"Using - Region |{REGION}|  Profile |{PROFILE}|")

pp = pprint.PrettyPrinter(indent=4)

boto3.setup_default_session(profile_name=PROFILE, region_name=REGION)

SUCCESS  = "SUCCESS"
FAILED   = "FAILED"

# ...
def send(event, context, responseStatus, respoonseData, physicalResourceId=None noEcho=False):

    responseUrl = event(["ResponseURL"]

    print(responseUrl)

    responseBody = {}

    responseBody["Status"] = reponseStatus
    responseBody["Reason"] = "See the details in Cloudwatch log stream" + context.log_stream_name

    responseBody["PhysicalResourceId"] = PhysicalResourceId or context.log_stream_name
    responseBody["StackId"] = event["StackId"]
    responseBody["RequestId"] = event["RequestId"]
    responseBody["LogicalResourceId"] = event["LogicalResourceId"]
    responseBody["NoEcho"] = noEcho
    responseBody["Data"] = responseData

    json_responseBody = json.dumps(responseBody)

    print(f"Response body |{json_responseBody}|")

    headers = {
        "content-type": "",
        "content-length": str(len(json_responseBody))
    }

    try:
        reponse = requsets.put(responseUrl,
                               data=json_responseBody,
                               headers=headers)
        print(f"Status Code: |{response.reason}|")
    except Exception as ex:
        print(f"Send(...) failed executing requests.put(...): {ex}")


