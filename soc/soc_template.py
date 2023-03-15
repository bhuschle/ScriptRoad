#!/usr/bin/env python3

import os
import os.path
import sys
import time
import json
import urllib
import requests
import argparse
import hashlib
import base64
from datetime import datetime

#...

# for terminal colors
class Colors:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  PURPLE = '\033[95m'
  ENDC = '\033[0m'

#...

class Lines:
  GOOD = Colors.GREEN + '[+] ' + Colors.ENDC
  OK = Colors.YELLOW + '[*] ' + Colors.ENDC
  BAD = Colors.RED + '[-] ' + Colors.ENDC
  VBAD = Colors.RED + '[!]' + Colors.ENDC
  NEUTRAL = Colors.BLUE + '[#] ' + Colors.ENDC
  UNEXPECTED = Colors.PURPLE + '[)()]' + Colors.ENDC
  SEP1 = '==========================================================================='
  SEP2 = '___________________________________________________________________________'

  def seven_liner(less, sus, mal, fail ,und , uns, tim):
    print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + 'HARMLESS', Colors.YELLOW + 'SUSPICIOUS', Colors.RED + 'MALICIOUS', 'FAILURE', Colors.BLUE + 'UNDETECTED', 'UNSUPPORTED', 'TIMEOUT' + Colors.ENDC))

    if mal > 0:
      print(Lines.BAD + '{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), str(fail), Colors.BLUE + str(und), str(tim), str(uns) + Colors.ENDC))
    elif sus > 0:
      print(Lines.OK + '{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), str(fail), Colors.BLUE + str(und), str(uns), str(und) + Colors.ENDC))
    elif und > 0 or tim > 0:
      print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), str(fail), Colors.BLUE + str(und), str(uns), str(und) + Colors.ENDC))
    else:
      print(Lines.GOOD + '{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), str(fail), Colors.BLUE + str(und), str(uns), str(und) + Colors.ENDC))

  def five_liner(less, sus, mal, und, tim):
    print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + 'HARMLESS', Colors.YELLOW + 'SUSPICIOUS', Colors.RED + 'MALICIOUS', Colors.BLUE + 'UNDETECTED', 'TIMEOUT' + Colors.ENDC))

    if mal > 0:
      print(Lines.BAD + '{:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), Colors.BLUE + str(und), str(tim) + Colors.ENDC))
    elif sus > 0:
      print(Lines.OK + '{:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), Colors.BLUE + str(und), str(tim) + Colors.ENDC))
    elif und > 0 or tim > 0:
      print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), Colors.BLUE + str(und), str(tim) + Colors.ENDC))
    else:
      print(Lines.GOOD + '{:18} {:18} {:18} {:18} {:18}'.format(Colors.GREEN + str(less), Colors.YELLOW + str(sus), Colors.RED + str(mal), Colors.BLUE + str(und), str(tim) + Colors.ENDC))

  def four_liner(item, name):
    if item == 'harmless':
          print(Lines.GOOD + name + Colors.GREEN + item + Colors.ENDC)
    elif item == 'suspicious':
      print(Lines.OK + name + Colors.YELLOW + item + Colors.ENDC)
    elif item == 'malicious':
      print(Lines.BAD + name + Colors.RED + item + Colors.ENDC)
    else:
      print(Lines.NEUTRAL + name + Colors.BLUE + item + Colors.ENDC)

  def rep_liner(rep):
    if rep == -100:
      print(Lines.VBAD + 'Reputation       : ' + Colors.RED + str(rep) + Colors.ENDC)
    elif rep > -100 and rep < -50:
      print(Lines.BAD + 'Reputation       : ' + Colors.RED + str(rep) + Colors.ENDC)
    elif rep >= -50 and rep < 50:
      print(Lines.OK + 'Reputation       : ' + Colors.YELLOW + str(rep) + Colors.ENDC)
    elif rep >= 50 and rep < 100:
      print(Lines.NEUTRAL + 'Reputation       : ' + Colors.BLUE + str(rep) + Colors.ENDC)
    elif rep == 100:
      print(Lines.GOOD + 'Reputation       : ' + Colors.GREEN + str(rep) + Colors.ENDC)
    else:
      print(Lines.UNEXPECTED + Colors.PURPLE + 'Reputation Result was not Expected!' + Colors.ENDC)
      print(Lines.UNEXPECTED + 'Reputation       : ' + Colors.PURPLE + str(rep) + Colors.ENDC)

  def two_liner_True(item, name):
    if item is True:
      print(Lines.BAD + name + Colors.GREEN + str(item) + Colors.ENDC)
    else:
      print(Lines.GOOD + name + Colors.RED +  str(item) + Colors.ENDC)

  def two_liner_False(item, name):
    if item is True:
      print(Lines.GOOD + name + Colors.GREEN + str(item) + Colors.ENDC)
    else:
      print(Lines.BAD + name + Colors.RED +  str(item) + Colors.ENDC)

  def vote_liner(v_less, v_mal):
    print(Lines.NEUTRAL + Colors.BLUE + 'Total Votes' + Colors.ENDC)
    print(Lines.GOOD + 'Harmless         : ' + Colors.GREEN + str(v_less) + Colors.ENDC)
    print(Lines.BAD +  'Malicious        : ' + Colors.RED + str(v_mal) + Colors.ENDC)

  def risk_liner(risk):
    if risk > 74:
      print(Lines.OK + 'Risk Score : ' + Colors.YELLOW + str(risk) + Colors.ENDC)
    if risk > 84:
      print(Lines.BAD + 'Risk Score : ' + Colors.RED + str(risk) + Colors.ENDC)
    elif risk == 100:
      print(Lines.VBAD + Colors.RED + 'Risk Score : ' + str(risk) + Colors.ENDC)
    else:
      print(Lines.GOOD + 'Risk Score : ' + Colors.GREEN + str(risk) + Colors.ENDC)
#...

# VirusTotal API key
VT_API_KEY = "[INSERT YOUR VIRUS TOTAL API HERE]"

# VirusTotal API v3 URL
VT_API_URL = "https://www.virustotal.com/api/v3/"

#...
class VTScan:
  def __init__(self):
    self.headers = {
      "accept": "application/json",
      "x-apikey" : VT_API_KEY
    }

  def url(self, url_path):
    self.url_path = url_path
    vt_id = str(base64.urlsafe_b64encode(url_path.encode()).decode().strip("="))
    vt_url = VT_API_URL + "urls/" + vt_id
    # print(vt_url)
    res = requests.get(vt_url, headers = self.headers)

    if res.status_code == 200:
      result = res.json()

      json_path = result.get("data").get("attributes")

      print(Colors.BLUE + Lines.SEP1)
      print(json_path.get("url"))
      print(json_path.get("title"))
      print(Lines.SEP1 + Colors.ENDC)

      print()
      print(Lines.NEUTRAL + Colors.BLUE + 'VirusTotal Scan :' + Colors.ENDC)
      print(Lines.NEUTRAL + str(datetime.fromtimestamp(json_path.get("last_analysis_date"))))

      red = json_path.get("redirection_chain")
      for item in red:
        print(Lines.NEUTRAL + item)

      las = json_path.get("last_analysis_stats")

      less = las.get("harmless")
      sus = las.get("suspicious")
      mal = las.get("malicious")
      und = las.get("undetected")
      tim = las.get("timeout")

      print()
      Lines.five_liner(less, sus, mal, und, tim)

      print()
      print(Lines.NEUTRAL + "Outgoing Links :")
      out = json_path.get("outgoing_links")
      for item in out:
        print(Lines.NEUTRAL + item)
      print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)
      print()

    else:
      print (Colors.RED + "FAILED :(" + Colors.ENDC)
      print (Colors.RED + "status code: " + str(res.status_code) + Colors.ENDC)

  def hash(self, h):
    self.h = h
    vt_url = "https://www.virustotal.com/api/v3/files/" + h

    res = requests.get(vt_url, headers = self.headers)

    if res.status_code == 200:
      result = res.json()

      json_path = result.get("data").get("attributes")

      print(Colors.BLUE + Lines.SEP1)
      print('Name   : ' + json_path.get("meaningful_name"))
      print('MD5    : ' + json_path.get("md5"))
      print('SHA1   : ' + json_path.get("sha1"))
      print('SHA256 : ' + json_path.get("sha256"))
      print(Lines.SEP1 + Colors.ENDC)

      print()
      print(Lines.NEUTRAL + Colors.BLUE + 'VirusTotal Scan :' + Colors.ENDC)
      print(Lines.NEUTRAL + str(datetime.fromtimestamp(json_path.get("last_analysis_date"))))
      print()


      print(Lines.NEUTRAL + Colors.BLUE + 'Associated Names : ' + Colors.ENDC)
      red = json_path.get("names")
      for item in red:
        print(Lines.NEUTRAL + item)

      rep = json_path.get("reputation")
      print()
      Lines.rep_liner(rep)      

      print()

      first = json_path.get("first_submission_date")
      last = json_path.get("last_analysis_date")
      dl = json_path.get("downloadable")
      size = json_path.get("size")
      t_sub = json_path.get("times_submitted")
      desc = json_path.get("type_description")
      ext = json_path.get("type_extension")
      tag = json_path.get("type_tag")

      print(Lines.NEUTRAL + 'First Submission : ' + str(datetime.fromtimestamp(first)))
      print(Lines.NEUTRAL + 'Last Analysis    : ' + str(datetime.fromtimestamp(last)))
      print(Lines.NEUTRAL + 'Times Submitted  : ' + str(t_sub))
      print(Lines.NEUTRAL + 'Downloadable     : ' + Colors.BLUE + str(dl) + Colors.ENDC)
      print(Lines.NEUTRAL + 'Size             : ' + str(size))
      print(Lines.NEUTRAL + 'Type Description : ' + desc)
      print(Lines.NEUTRAL + 'Type Extension   : ' + ext)
      print(Lines.NEUTRAL + 'Type Tag         : ' + tag)
      print()

      t_votes = json_path.get("total_votes")
      v_less = t_votes.get("harmless")
      v_mal = t_votes.get("malicious")

      Lines.vote_liner(v_less, v_mal)
      
      las = json_path.get("last_analysis_stats")

      less = las.get("harmless")
      sus = las.get("suspicious")
      mal = las.get("malicious")
      und = las.get("undetected")
      tim = las.get("timeout")
      uns = las.get("type-unsupported")
      fail = las.get("failure")

      print()
      print(Lines.NEUTRAL + Colors.BLUE + 'Last Analysis Results :' + Colors.ENDC)
      Lines.seven_liner(less, sus, mal, fail ,und , uns, tim)

      sigma = json_path.get("sigma_analysis_results")
      stat = json_path.get("sigma_analysis_stats")

      print()
      if sigma != None:
        for item in sigma:
          print(Lines.NEUTRAL + sigma.get("rule_title"))
          print(Lines.NEUTRAL + sigma.get("rule_source"))
          print(Lines.NEUTRAL + sigma.get("rule_level"))
          print(Lines.NEUTRAL + sigma.get("rule_description"))
          print(Lines.NEUTRAL + sigma.get("rule_author"))
          print(Lines.NEUTRAL + sigma.get("rule_id"))
        
        crit = stat.get("critical")
        high = stat.get("high")
        med = stat.get("medium")
        low = stat.get("low")

        print()
        print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18}'.format(Colors.RED + 'CRITICAL', 'HIGH', Colors.YELLOW + 'MEDIUM', Colors.BLUE + "LOW"))

        if crit > 0:
          print(Lines.VBAD + '{:18} {:18} {:18} {:18}'.format(Colors.RED + str(crit), str(high), Colors.YELLOW + str(med), Colors.BLUE + str(low) + Colors.ENDC))
        elif high > 0:
          print(Lines.BAD + '{:18} {:18} {:18} {:18}'.format(Colors.RED + str(crit), str(high), Colors.YELLOW + str(med), Colors.BLUE + str(low) + Colors.ENDC))
        elif med > 0:
          print(Lines.OK + '{:18} {:18} {:18} {:18}'.format(Colors.RED + str(crit), str(high), Colors.YELLOW + str(med), Colors.BLUE + str(low) + Colors.ENDC))
        else:
          print(Lines.NEUTRAL + '{:18} {:18} {:18} {:18}'.format(Colors.RED + str(crit), str(high), Colors.YELLOW + str(med), Colors.BLUE + str(low) + Colors.ENDC))
      else:
        print(Lines.NEUTRAL + Colors.BLUE + 'NO SIGMA RESULTS' + Colors.ENDC)

      print()

      link = json_path.get("links")
      print(Lines.NEUTRAL + Colors.BLUE + 'Link :' + Colors.ENDC)
      if link != None:
        print(Lines.NEUTRAL + str(link.get("self")))
      else:
        print(Lines.NEUTRAL + 'NO LINK AVAILABLE')

      print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)
      print()


    else: 
      print (Colors.RED + "FAILED :(" + Colors.ENDC)
      print (Colors.RED + 'Possibly No Matches Found!' + Colors.ENDC)
      print (Colors.RED + "status code: " + str(res.status_code) + Colors.ENDC)

  def ip(self, ip_addr):
    self.ip_addr = ip_addr

    vt_url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_addr

    res = requests.get(vt_url, headers = self.headers)

    if res.status_code == 200:
      result = res.json()

      json_path = result.get("data").get("attributes")

      print(Colors.BLUE + Lines.SEP1)
      print('{:10} {:1} {:10} {:10} {:1} {:10}'.format('Owner', ':', json_path.get("as_owner"), 'Continent', ':', json_path.get("continent")))
      print('{:10} {:1} {:10} {:10} {:1} {:10}'.format( 'ASN #', ':', str(json_path.get("asn")), 'Country', ':', json_path.get("country")))
      print(Lines.SEP1 + Colors.ENDC)

      print()
      print(Lines.NEUTRAL + Colors.BLUE + 'VirusTotal Scan :' + Colors.ENDC)
      print(Lines.NEUTRAL + str(datetime.fromtimestamp(json_path.get("last_analysis_date"))))


      las = json_path.get("last_analysis_results")
      cat = las.get("category")
      eng = las.get("engine_name")
      meth = las.get("method")
      resu = las.get("result")
      jarm = json_path.get("jarm")

      if cat != None:
        Lines.four_liner(cat, 'Category : ')
      if eng != None:
        print(Lines.NEUTRAL + 'Engine   : ' + eng)
      if meth != None:
        print(Lines.NEUTRAL + 'Method   : ' + meth)
      if resu != None:
        Lines.four_liner(resu, 'Result   : ')

      print(Lines.NEUTRAL + 'JARM     : ' + jarm)


      las = json_path.get("last_analysis_stats")

      less = las.get("harmless")
      sus = las.get("suspicious")
      mal = las.get("malicious")
      und = las.get("undetected")
      tim = las.get("timeout")

      print()
      Lines.five_liner(less, sus, mal, und, tim)

      net = json_path.get("network")
      reg_int = json_path.get("regional_internet_registry")
      rep = json_path.get("reputation")
      t_votes = json_path.get("total_votes")
      v_less = t_votes.get("harmless")
      v_mal = t_votes.get("malicious")
      ip_id = json_path.get("id")

      # REP is getting weird numbers, circle back on this one
      # REP for 8.8.8.8 is 504, Dont know how that is calculated or what the range is
      # print()
      # Lines.rep_liner(rep)
      print()
      Lines.vote_liner(v_less, v_mal)
      print()
      print(Lines.NEUTRAL + 'Network           : ' + str(net))
      print(Lines.NEUTRAL + 'Regional Internet : ' + reg_int)
      print(Lines.NEUTRAL + 'IP ID             : ' + str(ip_id))

      print()
      print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)
      print()
      
      print(Lines.NEUTRAL + Colors.BLUE + 'WHOIS Report :' + Colors.ENDC)
      print(str(datetime.fromtimestamp(json_path.get("whois_date"))))
      print(json_path.get("whois"))

      print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)
      print()



class IPQS:
  key = '[ENTER YOUR IP QUALITY SCORE API HERE]'

  def url(self, url: str, vars: dict = []) -> dict:
    url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
    x = requests.get(url, params = vars)

    res = x.json()
    
    age = res.get("domain_age")
    yrs = age.get("human")
    iso = age.get("timestamp")

    unsafe = res.get("unsafe")
    park = res.get("parking")
    red = res.get("redirected")
    dns = res.get("dns_valid")
    ip = res.get("ip_address")
    serv = res.get("server")

    cat = res.get("category")
    mal = res.get("malware")
    phis = res.get("phishing")
    spam = res.get("spamming")
    sus = res.get("suspicious")
    adult = res.get("adult")
    risk = res.get("risk_score")

    


    print(Lines.NEUTRAL + Colors.BLUE + 'IP Quality Score :' + Colors.ENDC)
    print(Lines.NEUTRAL + str(datetime.fromtimestamp(iso)))
    print(Lines.NEUTRAL + yrs)
    print()
    print(Lines.NEUTRAL + str(cat))
    print(Lines.NEUTRAL + ip)
    print(Lines.NEUTRAL + serv)
    print()

    Lines.risk_liner(risk)
    print()

    Lines.two_liner_False(dns, 'DNS Valid  : ')
    Lines.two_liner_True(unsafe, 'Unsafe     : ')
    Lines.two_liner_True(park, 'Parking    : ')
    Lines.two_liner_True(red, 'Redirected : ')

    print()
    
    Lines.two_liner_True(mal, 'Malware    : ')
    Lines.two_liner_True(phis, 'Phishing   : ')
    Lines.two_liner_True(spam, 'Spam       : ')
    Lines.two_liner_True(sus, 'Suspicious : ')
    Lines.two_liner_True(adult, 'Adult      : ')

    print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)

  def ip(self, ip_addr):
    url = 'https://www.ipqualityscore.com/api/json/ip/%s/%s' % (self.key, ip_addr)
    x = requests.get(url)

    res = x.json()

    ctry = res.get("country_code")
    tmzn = res.get("timezone")
    rgn = res.get("region")
    city = res.get("city")
    lat = res.get("latitude")
    lon = res.get("longitude")

    host = res.get("host")
    isp = res.get("ISP")
    req = res.get("request_id")

    fraud = res.get("fraud_score")

    crawler = res.get("is_crawler")
    mbl = res.get("mobile")
    prox = res.get("proxy")
    vpn = res.get("vpn")
    avpn = res.get("active_vpn")
    tor = res.get("tor")
    ator = res.get("active_tor")
    abuse = res.get("recent_abuse")
    bot = res.get("bot_status")

    print(Lines.NEUTRAL + Colors.BLUE + 'IP Quality Score :' + Colors.ENDC)
    print(Lines.NEUTRAL + '{:26} {:3} {:6} {:8}'.format(tmzn, city + ',', rgn + ',', ctry))
    print(Lines.NEUTRAL + '{:11} {:12} {:2} {:11} {:12}'.format('Latitude :', Colors.BLUE + str(lat) + Colors.ENDC, ' ', 'Longitude :', Colors.BLUE + str(lon) + Colors.ENDC))

    print()
    print(Lines.NEUTRAL + 'Host        : ' + Colors.BLUE + host + Colors.ENDC)
    print(Lines.NEUTRAL + 'ISP         : ' + Colors.BLUE + isp + Colors.ENDC)
    print(Lines.NEUTRAL + 'Request ID  : ' + Colors.BLUE + req + Colors.ENDC)

    print()
    Lines.risk_liner(fraud)

    print()
    Lines.two_liner_True(crawler, 'Crawler      : ')
    Lines.two_liner_True(mbl    , 'Mobile       : ')
    Lines.two_liner_True(prox   , 'Proxy        : ')
    Lines.two_liner_True(vpn    , 'VPN          : ')
    Lines.two_liner_True(avpn   , 'Active VPN   : ')
    Lines.two_liner_True(tor    , 'TOR          : ')
    Lines.two_liner_True(ator   , 'Active TOR   : ')
    Lines.two_liner_True(abuse  , 'Recent Abuse : ')
    Lines.two_liner_True(bot    , 'Bot          : ')

    print(Colors.BLUE + Lines.SEP2 + Colors.ENDC)
    print()

#...

#...



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description = 'SOCOPS investigation program using API, EDIT LINES 108 & 378 WITH API KEYS')
  parser.add_argument('-u', '--url', required = False, help = "Scans URL")
  parser.add_argument('-H', '--hash', required = False, help = "Scans MD5 / SHA1 / SHA256")
  parser.add_argument('-i', '--ip', required = False, help = "Scans IP Addresses")
  args = vars(parser.parse_args())
  vtscan = VTScan()
  ipqs = IPQS()

  os.system('clear && neofetch --source ~/.config/neofetch/GSclearSmall.txt --ascii_colors 7 8 2 1 1 1 --colors 2 7 7 2 7 7')

  if args["url"]:
    vtscan.url(args["url"])
    ipqs.url(args["url"], {})
  elif args["hash"]:
    vtscan.hash(args["hash"])
  elif args["ip"]:
    vtscan.ip(args["ip"])
    ipqs.ip(args["ip"])
