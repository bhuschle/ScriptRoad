#!/usr/bin/env python3

###############################################################################
# NAME: sumo-30day.py                                                         #
#                                                                             #
# VERSION: 20230405                                                           #
#                                                                             #
# SYNOPSIS: Checks for collectors that have been offline for more then 30     #
#           days, then deletes the collector.                                 #
#                                                                             #
# DESCRIPTION: The script first encodes the listed access key and id before   #
#               sending a request to each of the team-1 sumo clients and      #
#               deletes them from the collector list.                         #
#                                                                             #
# INPUT: None.                                                                #
#                                                                             #
# OUTPUT: 1.) STDOUT                                                          #
#                                                                             #
# PRE-RUNTIME NOTES: 1.) Rate limiting - A rate limit of four API requests    #
#                        per second (240 requests per minute) applies to all  #
#                        API calls from a user. A rate limit of 10 concurrent #
#                        requests to any API endpoint applies to an access    #
#                        key. This script throttles @ 2 calls/s.              #
#                    2.) The Sumo Logic API keys for your tenant need to be   #
#                        input in the init vars section.                      #
#                    3.) This script is only useful if you have collectors    #
#                        that are older then 30 days.                         #
#                                                                             #
# AUTHORS: GuardSight, Inc. (@guardsight) ; bhuschle@guardsight.com           #
#                                                                             #
# LICENSE: GPLv3                                                              #
#                                                                             #
# DISCLAIMER: All work produced by Authors is provided “AS IS”. Authors make  #
#             no warranties, express or implied, and hereby disclaims any and #
#             all warranties, including, but not limited to, any warranty of  #
#             fitness, application, et cetera, for any particular purpose,    #
#             use case, or application of this script.                        #
#                                                                             #
# (c) 2022 GuardSight, Inc.                                                   #
###############################################################################


# Import dependencies
import os
import os.path
import sys
import time 
import json
import requests
import base64

# API KEYS
# =================
## Chestnut
chestnut_access_id = 'suAsZLGn1kpOZB'
chestnut_access_key = 'RhwGHP45Yc3vH2JcB8AxZoMORLKIT9csvnSJ9EhWeRoQxDG5c536o4YciqNKKf2v'
## Canyonlands
canyonlands_access_id = 'supqyqbrQb0wrQ'
canyonlands_access_key = 'Mo8lzFnGPz3UHUTivTg7MyHiqHBPTU3TRqj8L7gKMtAtuOYE4hb5kSS1MkSQciN1'
## Holly
holly_access_id = 'sun4rUwpDKl5TL'
holly_access_key = 'MewJQvsIZ1aWclTaBbS2hxUs15ht9AhmAwjRpASlmbNAWRxvkp3VxEacUWBUQyW3'
## Ironwood
ironwood_access_id = 'suKLJ7tzrwVK38'
ironwood_access_key = 'maJU3YgAWHpskR06SwxjyXZC5hJg5XLQPsSzYejI9wXodijC6kBpciNpjSMZqINX'
## Oak
oak_access_id = 'suqYhQ17DsC4n6'
oak_access_key = 'Oq4obFBXx0L9TzpB74z2p6PoiCMDZet9fyZU4ka2BaAkvOcAGMG0ZDnquGujOKow'
## Yosemite
yosemite_access_id = 'sulRE3gDbWjROr'
yosemite_access_key = 'utBNpNsLShm7H8rfzmUO7HnM698Me9KlcxrM5H1RNqVNogktCCLpNvw2Je9rHtMX'
## Zion
zion_access_id = 'suzhNYdiysWwHp'
zion_access_key = 'pJa1AYF42MLQMQkQK7Hcj8GKqOrBKZVUFPQdARSK2eZZLwhNy4gdjszZegkbAOb1'

# Encode Access ID and Key so privacy is kept
def base64_encode(access_id, access_key):
  key = access_id + ':' + access_key
  key_bytes = key.encode("ascii")
  base64_bytes = base64.b64encode(key_bytes)
  base64_key = base64_bytes.decode("ascii")
  return base64_key

# GuardSight Logo printout
def print_logo():
  print()
  print('  %%%%%%%%%%%%%   %%%%%%%%%%%%%')
  print(' %%                           %%')
  print(' %%   #########   #########   %%')
  print(' %%  ##########   ##########  %%')
  print(' %%  #######################  %%')  
  print('             ##   ##   ')
  print('  %%   ###################   %%')
  print('   %%   #######   #######   %%')
  print('    %%   ######   ######   %%')
  print('     %%   #####   #####   %%')
  print('      %%   ####   ####   %%       Property of GuardSight, Inc')
  print('       %%               %%        Not to be redistributed without Authorization')
  print('        %%%%%%%   %%%%%%%         Author : bhuschle')  


# URL designation
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

# Print out Logo and information
print_logo()
print()
print('SUMO LOGIC - Collectors Offline for 30+ days')
print('--------------------------------------------')
print()

# Print out a response for each customer 
print('Chestnut    : ' + str(chestnut_res.status_code))
print('Canyonlands : ' + str(canyonlands_res.status_code))
print('Holly       : ' + str(holly_res.status_code))
print('Ironwood    : ' + str(ironwood_res.status_code))
print('Oak         : ' + str(oak_res.status_code))
print('Yosemite    : ' + str(yosemite_res.status_code))
print('Zion        : ' + str(zion_res.status_code))
