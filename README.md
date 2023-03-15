# ScriptRoad
Useful Scripts to use for everyday GS activities

## COTG

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


## Alienvault Scripts

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
