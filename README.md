# ScriptRoad
Useful Scripts to use for everyday GS activities

## COTG
### cotg.sh

Pretty straight forware COTG script  

two commands you can do is 
- cotg on
- cotg off [Transfer name]

Make sure to edit the cotg.sh and cotgoff.txt file with your personal information  
Also put the cotgoff.txt file inside of the same folder as your cotg.sh script  

add this to your .bash_aliases to be able to run from anywhere
```
cotg () {
  sh $HOME/[PATH TO PROGRAM FOLDER]/cotg/cotg.sh "$1" "$2"
}
```

## SOC

### soc.py

soc.py is a very thorough program that allows you to scan :
- IP Addresses
- Hash (MD5 / SHA1 / SHA256)
- URL Addresses

If you have any trouble running the program just use this command :
- soc -h
- soc --help

add this to your .bash_aliases to be able to run from anywhere
```
soc () {
  python3 $HOME/[PATH TO PROGRAM]/soc.py "$1" "$2"
}
```

API Keys can be gotten for this program for free from :
- https://www.virustotal.com/
  - Then create an account
  - Click on your profile
  - Click API
  - Copy API Key into soc.py line **116**
- https://www.ipqualityscore.com/
  - Register Account
  - Click on your account
  - Click View API Docs
  - Click Malicious URL Scanner
  - Scroll down until you see Private Key
  - Copy Private Key into soc.py line **386**

If you are having trouble running the program you probably need to install requests :
- sudo apt update
- sudo apt install python3-pip
- python -m pip install requests

I suggest using and making sure that python3 is installed on your system  
This is what I used to program the script so it will be smoother then python / python2 

## Alienvault

### av_match_sd.py

add this to your .bash_aliases to be able to run from anywhere  
```
av_sd () {
  clear
  python3 $HOME/[PATH TO PROGRAM]/av_match_sd.py ~/[PATH TO FOLDERS]/"$1"
}
```

Make sure to chmod +x global.py before you attempt to run it
 
When you run the command  
```
av_sd [FOLDER NAME WITH FILES INSIDE]
```

I personally make the folder name [mm-dd-yy] so that it is easy to remember and write  
Save files inside folder and then run script
