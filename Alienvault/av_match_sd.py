import csv
import sys
import os

YELLOW = "1;33;48m"
GREEN = '1;32;48m'
BLUE = '1;34;48m'
RED = '1;31;48m'
good = '[-]'
bad = '[+]'
ok = '[*]'

def dct(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

directory = sys.argv[1]

# Modify this list to match the deployments that you or your team deal with
dep_list = [LIST OF DEPLOYMENTS]


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
          print(dct(GREEN,good) ,dct(BLUE,'=========================================================================='))
          print(dct(GREEN,good) ,dct(BLUE,f'| \t {row["Method"]}'))
          print(dct(GREEN,good) ,dct(BLUE,'=========================================================================='))
          print(dct(GREEN,good))
          print(dct(GREEN,good) , dct(BLUE,"{0:50} {1}".format('Source', 'Destination')))

        if row["Deployment"] in dep_list:
          
          if row["Destinations"] == row["Sources"]:
            print(dct(GREEN,good) , dct(GREEN,"{0:50} {1}".format(row["Sources"], row["Destinations"])))
            accept_count += 1

          else:
            print(dct(RED,bad) , dct(RED,"{0:50} {1}".format(row["Sources"], row["Destinations"])))
            deny_count += 1
        
        line_count += 1

      if accept_count == 0 and deny_count == 0:
        print(dct(YELLOW,ok) , dct(BLUE,'_______________________________________________________________________________________'))
        print(dct(YELLOW,ok), dct(YELLOW,'NO ACCOUNTS TO REVIEW'))

      if accept_count == 0 and deny_count == 0:
        print(dct(YELLOW,ok) , dct(BLUE,'_______________________________________________________________________________________'))
        print(dct(YELLOW,ok) , "{1:50} {0:50} {2:50}".format(dct(BLUE,'Line Count : ') + dct(YELLOW,str(line_count)), dct(BLUE,'Accept Count : ') + dct(YELLOW,str(accept_count)), dct(BLUE,'Deny Count : ') + dct(YELLOW,str(deny_count))))
        print(dct(YELLOW,ok))
        if deny_count == 0 and accept_count == 0 and line_count > 0:
          print(dct(YELLOW,ok), dct(YELLOW,'MORE LINES READ THEN ACCEPTED OR DENIED - PLEASE MANUALLY REVIEW FILE'))
        print(dct(YELLOW,ok), dct(YELLOW,'Finished'))
      elif deny_count > 0:
        print(dct(RED,bad) , dct(BLUE,'_______________________________________________________________________________________'))
        print(dct(RED,bad) , "{1:50} {0:50} {2:50}".format(dct(BLUE,'Line Count : ') + dct(RED,str(line_count)), dct(BLUE,'Accept Count : ') + dct(RED,str(accept_count)), dct(BLUE,'Deny Count : ') + dct(RED,str(deny_count))))
        print(dct(RED,bad))
        if deny_count + accept_count < line_count:
          print(dct(RED,bad), dct(RED,'MORE LINES READ THEN ACCEPTED OR DENIED - PLEASE MANUALLY REVIEW FILE'))
        print(dct(RED,bad), dct(RED,'Finished'))
      else:
        print(dct(GREEN,good) , dct(BLUE,'_______________________________________________________________________________________'))
        print(dct(GREEN,good) , "{1:50} {0:50} {2:50}".format(dct(BLUE,'Line Count : ') + dct(GREEN,str(line_count)), dct(BLUE,'Accept Count : ') + dct(GREEN,str(accept_count)), dct(BLUE,'Deny Count : ') + dct(GREEN,str(deny_count))))
        print(dct(GREEN,good))
        if deny_count + accept_count < line_count:
          print(dct(GREEN,good), dct(GREEN,'MORE LINES READ THEN ACCEPTED OR DENIED - PLEASE MANUALLY REVIEW FILE'))
        print(dct(GREEN,good), dct(GREEN,'Finished'))

  print()
