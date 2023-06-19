#!/bin/bash

# Configuration variables
. /path/to/config.cfg
. /path/to/helper.sh

# Print colored output
print_color() {
  echo -e "$1 $2 $NC"
}

# Print line separator
print_line_sep() {
  echo -e "$YELLOW ________________________________________________________________$NC"
}

# Handle "on" operation
handle_on() {
  print_color $GREEN "Good $start_shift $user"
  print_color $BLUE "COTG - ON - VSOC_T1"
  print_line_sep
  {
    echo -e "[ $today ]"
    echo -e "# Acknowledging receipt of HOD transfer"
    echo -e "# Current Guardsight VSOC Team 1 HOD is $user\n"
  } | gpg --clearsign

  print_line_sep
  print_color $GREEN "HAVE A GOOD SHIFT $user"

}

# Handle "off" operation
handle_off() {
  print_color $GREEN "Good $start_shift $user"
  print_line_sep
  print_color $BLUE "COTG - OFF - VSOC_T1"
  {
    echo "[ $today ]"
    echo -e "[ COTG ]\n[ From -> To ]"
    echo -e "[ $user -> $1 ]\n"
    echo -e "[ Lookout ]\n$vsoc_lookout \n"
    echo -e "[ Notables ]\n$vsoc_notables\n"
    echo -e "[ Peer Review ]\n$vsoc_peer_review\n"
  } | gpg --clearsign

  print_line_sep
  print_color $BLUE "COTG - OFF - $arches"
  {
    echo "[ $today ]"
    echo -e "[ COTG ]\n[ From -> To ]"
    echo -e "[ $user -> $1 ]\n"
    echo -e "[ Lookout ]\n$arch_lookout\n"
    echo -e "[ Notables ]\n${arch_notables[0]}\n${arch_notables[1]}\n"
    echo -e "[ Peer Review ]\n$arch_peer_review\n"
  } | gpg --clearsign

  print_line_sep
  print_color $GREEN "HAVE A GOOD DAY $user"
}

# Main script
# Print header
print_heading "GuardSight Changing Of The Guard ( COTG )"

# Check input parameters
if [ "$1" = "on" ]; then
  handle_on
elif [ "$1" = "off" ]; then
  handle_off $2
else
  echo "Error: Invalid input parameter."
  exit 1
fi
