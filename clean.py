#!/usr/bin/env python3

import boto3
import os

CERTBOT_DOMAIN=os.environ['CERTBOT_DOMAIN']
CERTBOT_VALIDATION=os.environ['CERTBOT_VALIDATION']

client = boto3.Session(region_name='us-east-1').client('lightsail')
domainName='.'.join(CERTBOT_DOMAIN.split('.')[-2:]) # e.g., cirrascale.net
domainEntry={
  'name':'_acme-challenge.{}'.format(CERTBOT_DOMAIN),
  'target':'"{}"'.format(CERTBOT_VALIDATION),
  'type':'TXT',
}
response = client.delete_domain_entry(domainName=domainName, domainEntry=domainEntry)
print(response)
