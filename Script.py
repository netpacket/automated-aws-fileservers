#!/usr/bin/python
import sys
import random
import string

#subdomain algorithm
def randomString():
	domain = ""
	for x in range(0,8):
		if(random.randint(0,1) == 0):
			domain += random.choice(string.ascii_lowercase)
		else:
			domain += str(random.randint(0,9))
	return domain

#create subdomain	
subDomain = randomString()

#file changes
seaFile = open("/home/ubuntu/seafile-server/conf/seahub_settings.py",'r')
text = seaFile.read()
text = text.replace("https://foo.bar/seafhttp", "https://"+ subDomain + ".dr0ppin.science/seafhttp")
seaFile.close()
seaFile = open("/home/ubuntu/seafile-server/conf/seahub_settings.py", 'w')
seaFile.write(text)
seaFile.close()

ccnet = open("/home/ubuntu/seafile-server/conf/ccnet.conf", 'r')
ccnet_conf = ccnet.read()
ccnet_conf = ccnet_conf.replace("foo.bar", "https://" + subDomain + ".dr0ppin.science")
ccnet.close()
ccnet = open("/home/ubuntu/seafile-server/conf/ccnet.conf", 'w')
ccnet.write(ccnet_conf)
ccnet.close()

nginx = open("/etc/nginx/sites-enabled/seafile.conf", 'r')
conf = nginx.read()
conf = conf.replace("foo.bar", subDomain + ".dr0ppin.science")
nginx.close()
nginx = open("/etc/nginx/sites-enabled/seafile.conf", 'w')
nginx.write(conf)
nginx.close()
