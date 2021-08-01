#!/bin/bash
echo $#

if [ $# -eq 0 ] #if the number of argument equals 0 that menas no databse name was passed. Raise an error.
then
    raise error "Invalid number of arguments"
else
    # iterate through name of each database passed as args and download its metadata
    for db_name in "$@"
    do
        echo "Table name passed   $db_name"
        python3 download_table_metadata.py $db_name > metadata.json

        # create new Database in Target Account
        aws dynamodb create-table --cli-input-json file://metadata.json
    done
fi


