#!/bin/bash

# Input file
input_file=$1

# Extract date from input file name
input_date=$(echo $input_file | grep -oP '\d{2}-\d{2}-\d{4}')

# Output file
output_file="Omni_report_$input_date.txt"

# Empty the output file
> $output_file

# Declare an array of asset names to search for
declare -a assets=('harborfreight' 'hearst' 'aquestive' 'radiustoday' 'intelerad' 'thrivemarket' 'sundance' 'red8' 'karman' 'karman-sd' 'athene' 'guardsight' 'jt4' 'jt4llc')

# Create an associative array to keep track of the URLs that have already been printed
declare -A printed_urls

# Set color for headers
BLUE='\033[0;34m'
RED='\033[0;33m'
NC='\033[0m' # No Color

# Loop over each asset
for asset in "${assets[@]}"
do
    # Print the asset name as a header to the output file with color
    echo -e "${BLUE}Asset Name: $asset${NC}" >> $output_file
    echo -e "${RED}---------------------${NC}" >> $output_file

    # Search the file for lines containing the asset name and do not contain 'new hits'
    # Append these lines to the output file
    results=$(grep -i "$asset" $input_file | grep -iv 'new hits')
    IFS=$'\n' # set delimiter
    for line in $results
    do
        # Use awk to split line into columns based on '|' separator
        # Then use printf to format each line based on the number of columns
        url=$(echo $line | awk -F '|' '{ print $1 }' | sed 's/^ *//;s/ *$//' | sed 's/^[0-9]*\. //')

        # Check if the URL has already been printed
        if [ -z "${printed_urls[$url]}" ]
        then
            # If not, print the URL and add it to the associative array of printed URLs
            echo $url >> $output_file
            printed_urls[$url]=1
        fi
    done

    # Print a newline for formatting
    echo "" >> $output_file
done
