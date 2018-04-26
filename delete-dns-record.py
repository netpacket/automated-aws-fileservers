#!/usr/bin/python
#open source Cloudflare python script and modified for this Capstone project
import sys
import string
import CloudFlare
import re

def main():
    zone_name = 'dr0ppin.science'
    
    cf = CloudFlare.CloudFlare(email='<value>', token='<value>')
    flag = ""
    dns_id = ""
    zone_temp = ""

    #grab variable flag for dns record id
    seaFile = open("/home/ubuntu/seafile-server/conf/seahub_settings.py",'r')
    text = seaFile.read()
    match = re.search(".........d0ppin.science", text)
    varFlag=match.group(0)
    
    # query for the zone name and expect only one value back
    try:
        zones = cf.zones.get(params = {'name':zone_name,'per_page':1})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones.get %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zones.get - %s - api call failed' % (e))

    if len(zones) == 0:
        exit('No zones found')

    # extract the zone_id which is needed to process that zone
    zone = zones[0]
    zone_id = zone['id']

    # request the DNS records from that zone
    try:
        dns_records = cf.zones.dns_records.get(zone_id)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

    # print the results - first the zone name
#    print zone_id, zone_name

    # then all the DNS records for that zone
    for dns_record in dns_records:
        r_name = dns_record['name']
        r_type = dns_record['type']
        r_value = dns_record['content']
        r_id = dns_record['id']
        r_zone = dns_record['zone_id']


	if r_name == varFlag:
           dns_id = r_id  
           zone_temp = r_zone
           break
    cf.zones.dns_records.delete(zone_temp, dns_id)
    exit(0)

if __name__ == '__main__':
    main()
