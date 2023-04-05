#!/usr/bin/env python3
# Script used to remove any agents that are Stale, AKA older then 30 days
# Script creator : bhuschle
# Authorized and Requested by : TClements

import os
import os.path
import sys
import time 
import json
import requests
import base64

chestnut_access_id = 'suAsZLGn1kpOZB'
chestnut_access_key = 'RhwGHP45Yc3vH2JcB8AxZoMORLKIT9csvnSJ9EhWeRoQxDG5c536o4YciqNKKf2v'

canyonlands_access_id = 'supqyqbrQb0wrQ'
canyonlands_access_key = 'Mo8lzFnGPz3UHUTivTg7MyHiqHBPTU3TRqj8L7gKMtAtuOYE4hb5kSS1MkSQciN1'

holly_access_id = 'sun4rUwpDKl5TL'
holly_access_key = 'MewJQvsIZ1aWclTaBbS2hxUs15ht9AhmAwjRpASlmbNAWRxvkp3VxEacUWBUQyW3'

ironwood_access_id = 'suKLJ7tzrwVK38'
ironwood_access_key = 'maJU3YgAWHpskR06SwxjyXZC5hJg5XLQPsSzYejI9wXodijC6kBpciNpjSMZqINX'

oak_access_id = 'suqYhQ17DsC4n6'
oak_access_key = 'Oq4obFBXx0L9TzpB74z2p6PoiCMDZet9fyZU4ka2BaAkvOcAGMG0ZDnquGujOKow'

yosemite_access_id = 'sulRE3gDbWjROr'
yosemite_access_key = 'utBNpNsLShm7H8rfzmUO7HnM698Me9KlcxrM5H1RNqVNogktCCLpNvw2Je9rHtMX'

zion_access_id = 'suzhNYdiysWwHp'
zion_access_key = 'pJa1AYF42MLQMQkQK7Hcj8GKqOrBKZVUFPQdARSK2eZZLwhNy4gdjszZegkbAOb1'

def base64_encode(access_id, access_key):
  key = access_id + ':' + access_key
  key_bytes = key.encode("ascii")
  base64_bytes = base64.b64encode(key_bytes)
  base64_key = base64_bytes.decode("ascii")
  return base64_key


url_1 = 'https://api.us2.sumologic.com/api/v1/collectors/offline?aliveBeforeDays=30'
url_2 = 'https://api.sumologic.com/api/v1/collectors/offline?aliveBeforeDays=30'

# setup all of the headers for each customer API
chestnut_headers  = { 'Authorization' : 'Basic ' + base64_encode(chestnut_access_id, chestnut_access_key) }
canyonlands_headers  = { 'Authorization' : 'Basic ' + base64_encode(canyonlands_access_id, canyonlands_access_key) }
holly_headers  = { 'Authorization' : 'Basic ' + base64_encode(holly_access_id, holly_access_key) }
ironwood_headers  = { 'Authorization' : 'Basic ' + base64_encode(ironwood_access_id, ironwood_access_key) }
oak_headers  = { 'Authorization' : 'Basic ' + base64_encode(oak_access_id, oak_access_key) }
yosemite_headers  = { 'Authorization' : 'Basic ' + base64_encode(yosemite_access_id, yosemite_access_key) }
zion_headers  = { 'Authorization' : 'Basic ' + base64_encode(zion_access_id, zion_access_key) }

# Send the request to delete all collectors more then 30 days old
chestnut_res = requests.delete(url_1, headers=chestnut_headers)
canyonlands_res = requests.delete(url_1, headers=canyonlands_headers)
holly_res = requests.delete(url_1, headers=holly_headers)
ironwood_res = requests.delete(url_1, headers=ironwood_headers)
oak_res = requests.delete(url_2, headers=oak_headers)
yosemite_res = requests.delete(url_2, headers=yosemite_headers)
zion_res = requests.delete(url_1, headers=zion_headers)

# Print out a response for each customer 
print('Chestnut    : ' + str(chestnut_res.status_code))
print('Canyonlands : ' + str(canyonlands_res.status_code))
print('Holly       : ' + str(holly_res.status_code))
print('Ironwood    : ' + str(ironwood_res.status_code))
print('Oak         : ' + str(oak_res.status_code))
print('Yosemite    : ' + str(yosemite_res.status_code))
print('Zion        : ' + str(zion_res.status_code))

# Testing
#print(oak_res.text)
#print(yosemite_res.text)

