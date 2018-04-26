#!/bin/bash

#sets the A record

#parameters for the curl request
auth_email="<value>"
auth_key=<value> # found in cloudflare account settings

#sets the next curl's variables
ip=$(curl -s http://ipv4.icanhazip.com)
domain=$(egrep -o ".........dr0ppin.science" /home/ubuntu/seafile-server/conf/seahub_settings.py)

#Cloudflare request for new A record
curl -X POST "https://api.cloudflare.com/client/v4/zones/<dns zone>/dns_records" \
     -H "X-Auth-Email:$auth_email" \
     -H "X-Auth-Key:$auth_key" \
     -H "Content-Type:application/json" \
     --data '{"type":"A","name":"'$domain'","content":"'$ip'","ttl":120,"priority":10,"proxied":true}'

