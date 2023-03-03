#!/bin/sh

today=$(date +%F)

# This is the directory that you have your cotgoff txt file in that you can edit
input="$HOME/[PATH TO TXT FILE]/cotgoff.txt"

# Start Shift Options       End Shift Options
## Morning                  Morning
## Afternoon                Afternoon
## Evening                  Evening
start_shift="[YOUR SHIFT START]"
end_shift="[YOUR SHIFT END]"

# VSOC TEAM
vsoc="[VSOC NUMBER]"

# Company Codename
code_1="[CODENAME 1]"
code_2="[CODENAME 2]"

# Variables
## $user is your username
## $on_off is whether or not you are COTGON or COTGOFF
## $user_off is the username of the person you are transferring to
### This variable will only be used during COTGOFF never on COTGON
user="[YOUR USERNAME]"
on_off=$1
user_off=$2

# KEEP THIS VARIABLE AT 0
cotg=0

# Look up bash colors and change to what you want to 
col_1='\033[1;32;48m' # GREEN
col_2='\033[1;33;48m' # YELLOW
col_3='\033[1;31;48m' # RED
col_4='\033[1;34;48m' # BLUE
col_5='\033[00m'      # BLACK

if [ "$on_off" = on ]; then
  
  # Take over COTG at start of shift
  # Echo message to $user and encrypt with gpg
  echo "$col_1"
  echo "Good $start_shift $user"
  echo "$col_4"
  echo "COTG - ON - $vsoc"
  echo "_________________________________________________"
  echo "$col_5"
  {
  echo "[$today]"
  echo "# Acknowledging receipt of HOD transfer"
  echo "# Current Guardsight VSOC Team 1 HOD is $user"
  echo " "
  }>tempfile.txt
  cat tempfile.txt | gpg --clearsign
  echo "$col_4"
  echo "_________________________________________________"
  echo "$col_1"
  echo "HAVE A GOOD SHIFT $user"
  echo "$col_5"

  # Remove the temp files so that they do not clutter
  rm -r tempfile.txt

elif [ "$on_off" = off ]; then

  # Give up COTG at end of shift
  # Echo VSOC message to $user and encrypt with gpg
  echo "$col_1"
  echo "Good $start_shift $user"
  echo "$col_4"
  echo "COTG - OFF - $vsoc"
  echo "_________________________________________________"
  echo "$col_5"

  # VSOC COTG OFF
  {
  echo "[$today]"
  echo "[COTG]"
  echo ""
  echo "[Changed From -> To]"
  echo "# bhuschle ->"
  echo "Primary: $user_off"
  echo "Secondary: Team"

  echo " "

  while IFS= read -r line; do
    if [ "$line" = VSOC ]; then
      cotg=0
      continue
    elif [ "$line" = SANDSTONE ]; then
      cotg=1
      continue
    elif [ "$line" = ARCHES ]; then
      cotg=2
      continue
    else
      if [ $cotg -eq 0 ]; then
        echo "$line"
      else
        continue
      fi
    fi
  done < "$input"

  echo " "
  }>tempfile1.txt
  cat tempfile2.txt | gpg --clearsign
  echo "$col_4"
  echo "_________________________________________________"
  echo "$col_2"

  # Echo SANDSTONE message to $user and encrypt with gpg
  echo "COTG - OFF - $code_1"
  echo "_________________________________________________"
  echo "$col_5"

  # SANDSTONE COTG OFF
  {
  echo "[$today]"
  echo "[COTG]"
  echo ""
  echo "[Changed From -> To]"
  echo "# bhuschle ->"
  echo "Primary: $user_off"
  echo "Secondary: Team"

  echo " "

  while IFS= read -r line; do
    if [ "$line" = VSOC ]; then
      cotg=0
      continue
    elif [ "$line" = SANDSTONE ]; then
      cotg=1
      continue
    elif [ "$line" = ARCHES ]; then
      cotg=2
      continue
    else
      if [ $cotg -eq 1 ]; then
        echo "$line"
      else
        continue
      fi
    fi
  done < "$input"

  echo " "
  }>tempfile2.txt
  cat tempfile2.txt | gpg --clearsign
  echo "$col_2"
  echo "_________________________________________________"
  echo "$col_3"

   # Echo SANDSTONE message to $user and encrypt with gpg
  echo "COTG - OFF - $code_2"
  echo "_________________________________________________"
  echo "$col_5"

  # SANDSTONE COTG OFF
  {
  echo "[$today]"
  echo "[COTG]"
  echo ""
  echo "[Changed From -> To]"
  echo "# bhuschle ->"
  echo "Primary: $user_off"
  echo "Secondary: Team"

  echo " "

  while IFS= read -r line; do
    if [ "$line" = VSOC ]; then
      cotg=0
      continue
    elif [ "$line" = SANDSTONE ]; then
      cotg=1
      continue
    elif [ "$line" = ARCHES ]; then
      cotg=2
      continue
    else
      if [ $cotg -eq 2 ]; then
        echo "$line"
      else
        continue
      fi
    fi
  done < "$input"

  echo " "
  }>tempfile3.txt
  cat tempfile3.txt | gpg --clearsign
  echo "$col_3"
  echo "_________________________________________________"
  echo "$col_1"
  echo "HAVE A GOOD DAY $user"
  echo "$col_5"

  # Remove the temp files so that they do not clutter
  rm -r tempfile1.txt
  rm -r tempfile2.txt
  rm -r tempfile3.txt
fi
