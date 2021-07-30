#!/bin/bash

Output=$(python3 read_state.py)
# echo $Output
if [[ $Output = "Start" ]]
then
    python3 download_dynamodb_tables.py
    # get current epoch time [6 digits]
    TIME_NOW=$(date +%s)
    # get all files from Source Bucket
    aws s3 sync s3://$SOURCE_BUCKET_NAME ./BackupFolder
    # zip all files in Current Folder
    cd BackupFolder
    zip  ../$TIME_NOW.zip .
    cd ..
    # upload zip file to Target Bucket
    aws s3 cp  $TIME_NOW.zip s3://$TARGET_BUCKET_NAME
else
    raise error "Error copying files to s3 bucket"
fi



