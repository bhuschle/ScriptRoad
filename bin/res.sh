#!/bin/bash

# Source the helper.sh file
source /path/to/helper.sh

# Define the menu options
options=(
  "Proofpoint"
  "Fortigate"
  "DLP Blocked"
  "Password Spray"
  "Web Investigation"
)

# Function to copy the selected text to the clipboard
copy_to_clipboard() {
  local text="$1"
  echo "$text" | xclip -selection clipboard
  echo "Copied to clipboard: $text"
}

# Function to display the menu
display_menu() {
  for ((i=0; i<${#options[@]}; i++)); do
    echo "$(($i+1)). ${options[$i]}"
  done
  echo ""
}

# Main program
print_heading "Holy Grail of Responses to GS Tickets"

while true; do
  display_menu

  read -p "Enter your choice (1-${#options[@]}): " choice

  if [[ $choice =~ ^[0-9]+$ ]] && ((choice >= 1 && choice <= ${#options[@]})); then
    selected_option=${options[$((choice-1))]}
    case $selected_option in
      "Proofpoint")
        copy_to_clipboard "TO: [EMAIL ADDRESS]
CC: socops@harborfreight.com
Subject Line: Malicious Email Delivered

Hello,

On $(date), you received an email that has a high probability of being malicious.

Sender: [FROM: EMAIL ADDRESS]
Subject: [EMAIL SUBJECT]

Please delete the email without opening it. If you have any questions or concerns, please contact socops@harborfreight.com.

Regards,"
        ;;
      "Fortigate")
        copy_to_clipboard "Notes:
- Connections were denied by Fortigate
- No outbound traffic to IP
- Broad attack across multiple targets and ports
- Part of ongoing activity from this IP against multiple targets
- No Surrounding IOCs
- IOC Negative
- Closing Ticket"
        ;;
      "DLP Blocked")
        copy_to_clipboard "Notes:
- Blocked
- Known HTTPS slip through VSOC rules
Analysis :
- IOC Negative
- Closing Ticket"
        ;;
      "Password Spray")
        copy_to_clipboard "Notes :
- Failed password spray attack
- [#] log in attempts using varying usernames
- Source IP is known abuser
- No evidence of successful login
Analysis :
- IOC Negative
- Closing Ticket"
        ;;
      "Web Investigation")
        copy_to_clipboard "ALCON,

Upon the conclusion of our investigation into the website https://, we have found { NO / SOME / MANY} malicious indicators.

The Website has a {NEUTRAL / NEGATIVE} disposition amongst OSINT sources.

Note: The Socops team is not versed in the company's policies and is uncertain if the website may violate any policies. The Socops team does not have the authority to approve or deny websites for the environment. We can, however, provide an assessment of the website in question.

Please reach out to socops@harborfreight.com if you have further questions.

Regards,"
      ;;
    esac
    break
  else
    echo "Invalid choice. Please enter a number from 1 to ${#options[@]}."
  fi
done
