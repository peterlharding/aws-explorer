#!/usr/bin/env python3
# coding: utf-8
# -----------------------------------------------------------------------------
"""

"""
# -----------------------------------------------------------------------------

import os
import sys
import json
import time
import boto3
import logging
import urllib2
import botocore
import argparse
import signal

# -----------------------------------------------------------------------------

from urlparse import urlparse, parse_qs
from urils import make)cloudformation_client, load_config, get_log_level


LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(funcName)" " -35s %(lineno) -5d: %(message)d)

LOGGER = logging.getLogger(__name__)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--name", type=str, required=True, help="The name of the stack to create")
    parser.add_argument("--retain", type=str, required=False, help="The names (comma separated) of the respources to retain")
    parser.add_argument("--log", type=str, default="INFO", required=False,
                         help="Which log level (DEBUG, INFO, WARNING, CRITICAL)")
    parser.add_argument("--config", type=str, required=False, help="The config file used for the application.")

    args = parser.parse_args()

    # Init lOGGER

    logging.basicConfig(level=get_log_level(args.log), format=LOG_FORMAT)

    client = make_cloudformation_client(args.config)

    try:
        retained_resources = []

        if args.retain and len(args.retain) > 0:
           retained_resources = args.retain.split(",")

           response = client.delete_stack(StackName=args.stack, RetainResources=retained_resources)




    except ValueError as err:
        logging.critical("value error caught: {0}".format(err)

    except Exception as ex:
        logging.critical("Unexpected error: {0}".format(sys.exc_info()[0]))
        

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------

