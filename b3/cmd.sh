#!/bin/sh
#
#  Purpose:  Examine various AWS properties
#
# -----------------------------------------------------------------------------


aws servicecatalog scan-provisioned-products
aws servicecatalog search-products
aws autoscaling describe-autoscaling-groups
aws autoscaling describe-autoscaling-groups | grep AutoScaling

aws ecs describe-clusters --cluster xxxxx
aws ecs list-attributes --target-type container-instance
aws ecs list-attributes --cluster xxxx --target-type container-instance

