#!/usr/bin/python3
import requests
import json
import os

# Disable SSL Warnings
requests.packages.urllib3.disable_warnings()

with open('config.json') as f:
   config = json.load(f)
unifiBasePath = 'https://localhost:8443'

loginReqUrl = unifiBasePath + '/api/login'
loginReqPostBody = {"strict":"true","password":config['password'],"remember":"false","username":config['username']}

loginReq = requests.post(loginReqUrl, json = loginReqPostBody, verify=False)

if (loginReq.json()['meta']['rc'] == 'ok'):
    #print('Successful login!')

    updateCheckUrl = unifiBasePath + '/api/s/default/stat/fwupdate/latest-version'
    updateCheckReq = requests.get(updateCheckUrl, cookies = loginReq.cookies, verify=False)
    updateDetails = updateCheckReq.json()['data'][0]
    if updateDetails['has_upgradable_controller']:
        print("Upgrade to Version " + updateDetails['latest'] + " available!")
        unifiDebFile = "unifi_controller_" + updateDetails['latest'] + ".deb"
        print("Downloading new Unifi Controller")
        os.system("wget -O "+unifiDebFile+" " + updateDetails['download_link'])
        print("Installing new Unifi Controller")
        os.system("sudo DEBIAN_FRONTEND=noninteractive dpkg -i " + unifiDebFile)
        print("Fixing possibly broken packages")
        os.system("sudo apt install --fix-broken -y")
        print("Upgraded Unifi Controller to Version " + updateDetails['latest'] + " successfully!")
    else:
        print("No update available!");
