import csv
import sys
import os

YELLOW = "1;33;48m"
GREEN = '1;32;48m'
RED = '1;31;48m'
good = '[-]'
bad = '[+]'
ok = '[*]'

def dct(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

directory = sys.argv[1]

# Modify this list to match the deployments that you or your team deal with
dep_list = ['cn://guardsight-bristlecone-1.alienvault.cloud', 'cn://guardsight-buckeye-1.alienvault.cloud', 'cn://guardsight-zion-1.alienvault.cloud', 'cn://guardsight-redwood-1.alienvault.cloud', 'cn://guardsight-olympic-1.alienvault.cloud', 'cn://guardsight-congaree-1.alienvault.cloud']


for filename in os.listdir(directory):

  print()

  file = os.path.join(directory,filename)

  if os.path.isfile(file):

    print(dct(GREEN,'==========================================================================================='))
    print(dct(GREEN, filename))
    print(dct(GREEN,'==========================================================================================='))
    print()

    with open(file, mode='r') as csv_file:
      
      csv_reader = csv.DictReader(csv_file)
      line_count = 0
      accept_count = 0
      deny_count = 0

      for row in csv_reader:
          
        if line_count == 0:
          print(dct(GREEN,good) ,'==========================================================================')
          print(dct(GREEN,good) ,f'| \t {row["Method"]}')
          print(dct(GREEN,good) ,'==========================================================================')
          print(dct(GREEN,good))
          print(dct(GREEN,good) , "{0:50} {1}".format('Source', 'Destination'))

        if row["Deployment"] in dep_list:
          
          if row["Destinations"] == row["Sources"]:
            print(dct(GREEN,good) , "{0:50} {1}".format(row["Sources"], row["Destinations"]))
            accept_count += 1

          else:
            print(dct(RED,bad) , "{0:50} {1}".format(row["Sources"], row["Destinations"]))
            deny_count += 1
        
        line_count += 1

      if accept_count == 0 and deny_count == 0:
        print(dct(YELLOW,ok) , '_______________________________________________________________________________________')
        print(dct(YELLOW,ok), 'No Accounts needed to review ')

      if accept_count == 0 and deny_count == 0:
        print(dct(YELLOW,ok) , '_______________________________________________________________________________________')
        print(dct(YELLOW,ok) , "{1:50} {0:50} {2:50}".format('Line Count : ' + dct(YELLOW,str(line_count)), 'Accept Count : ' + dct(YELLOW,str(accept_count)), 'Deny Count : ' + dct(YELLOW,str(deny_count))))
        if deny_count == 0 and accept_count == 0 and line_count > 0:
          print(dct(YELLOW,ok), dct(YELLOW,'NO ACCEPTIONS OR DENYS - PLEASE MANUALLY REVIEW FILE'))
        print(dct(YELLOW,ok), dct(YELLOW,'Finished'))
      elif deny_count > 0:
        print(dct(RED,bad) , '_______________________________________________________________________________________')
        print(dct(RED,bad) , "{1:50} {0:50} {2:50}".format('Line Count : ' + dct(RED,str(line_count)), 'Accept Count : ' + dct(RED,str(accept_count)), 'Deny Count : ' + dct(RED,str(deny_count))))
        if deny_count + accept_count < line_count:
          print(dct(RED,bad), dct(RED,'MORE LINES READ THEN ACCEPTED OR DENIED - PLEASE MANUALLY REVIEW FILE'))
        print(dct(RED,bad), dct(RED,'Finished'))
      else:
        print(dct(GREEN,good) , '_______________________________________________________________________________________')
        print(dct(GREEN,good) , "{1:50} {0:50} {2:50}".format('Line Count : ' + dct(GREEN,str(line_count)), 'Accept Count : ' + dct(GREEN,str(accept_count)), 'Deny Count : ' + dct(GREEN,str(deny_count))))
        if deny_count + accept_count < line_count:
          print(dct(GREEN,good), dct(GREEN,'MORE LINES READ THEN ACCEPTED OR DENIED - PLEASE MANUALLY REVIEW FILE'))
        print(dct(GREEN,good), dct(GREEN,'Finished'))

  print()
