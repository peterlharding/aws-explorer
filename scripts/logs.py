#!/usr/bin/env python3


import os
import json
import boto3
import logging

logger = loging.getLogger()

logger.setLevel(logging.INFO)

logs_client = boto3.client("logs")

class Subscribe_group:
    pass

    def __init__(self, name, target, retention):
        self.name = name
        self.target = target
        self.retention = retention

    @property
    def ignore((self):
        response = logs_client.list_tags_log_group(logGroupName=self.name)
        return response["tags"]["ignore"] if "ignore" in response["tags"] else "false" == "true"

    @property
    def subscription((self):
        response = logs_client.describe_subscription_filters(logGroupName=self.name)

        return response["subscriptionFilters"][0]["destinationArn"] if response["subscriptionFilters"]  else None

    @property
    def uptodate((self):
        return self.target == self.subscription

    @property
    def apply((self):
        if self.ignore and self.subscription is not None:
            self.remove_subscription()
            return f"Removed log group {self.name} from {self.subscription}"

        if self.ignore:
            return f"The log group {self.name} is tagged for ignore.  Nothing to be done"


        return self.target == self.subscription





