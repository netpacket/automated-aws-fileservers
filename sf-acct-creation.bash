#!/bin/bash

#searches for the new website for seafile curl parameters
domain=$(egrep -o "........dr0ppin.science" /home/ubuntu/seafile-server/conf/seahub_settings.py)

#grabs the token
token=$(curl -d "username=<value>&password=<value>" "https://${domain}/api2/auth-token/")

#removes the json format
token=$(echo $token | tr -cd "[:alnum:]" | tr -d "tokn")
token="${token:1}"

#creates the temporary password
cat > passGenerator.py <<- EOF
import random
import string
domain = ""
for x in range(0,8):
    if(random.randint(0,1)==0):
        domain += random.choice(string.ascii_letters)
    else:
        domain += str(random.randint(0,9))
print(domain)
EOF
PASSW=$(python passGenerator.py)
rm passGenerator.py

#curl command to create the account 
curl -v -X PUT -d "password=1234" -H "Authorization: Token ${token}" -H 'Accept: application/json; indent=4' https://${domain}/api2/accounts/"test@gmail.com"
