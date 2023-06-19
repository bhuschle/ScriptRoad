print_heading() {
    local heading="$1"

    local bold_blue="\e[1;34m"
    local bold_magenta="\e[1;35m"
    local bold_red="\e[1;31m"
    local reset="\e[0m"

    echo ""
    echo -e "${bold_blue}    ██████╗  █████╗ ██████╗  ██████╗ ███████╗██████╗${reset}"
    echo -e "${bold_blue}    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔══██╗${reset}"
    echo -e "${bold_blue}    ██████╔╝███████║██║  ██║██║  ███╗█████╗  ██████╔╝${reset}"
    echo -e "${bold_blue}    ██╔══██╗██╔══██║██║  ██║██║   ██║██╔══╝  ██╔══██╗${reset}"
    echo -e "${bold_blue}    ██████╔╝██║  ██║██████╔╝╚██████╔╝███████╗██║  ██║${reset}"
    echo -e "${bold_blue}    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝${reset}"
    echo -e "${bold_magenta}    ----------------------------------------------------${reset}"
    echo ""
    echo -e "${bold_magenta}    $heading${reset}"
    echo -e "${bold_blue}    This file is the property of ${bold_red}bhuschle${reset}"
    echo -e "${bold_blue}    Do ${bold_red}NOT ${bold_blue}distribute without permission${reset}"
    echo -e "${bold_magenta}    ----------------------------------------------------${reset}"
    echo ""
}
