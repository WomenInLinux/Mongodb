#!/bin/python3.6

import boto3

ec2 = boto3.resource('ec2')
response = ec2.Vpc('vpc-20e5f259')
info = response.state
print(info)


cidr_blocks = response.cidr_block
print(cidr_blocks)


instancetenancy = response.instance_tenancy
print(instancetenancy)


vpcid = response.vpc_id
print(vpcid)
