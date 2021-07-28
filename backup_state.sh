#!/bin/bash

Output=$(python3 read_table_dynamodb.py)
# echo $Output
if [[ $Output = "Start" ]]
then
    # Environment variables
    # SOURCE_BUCKET_NAME=shivam-terraform-state-backend-1212121
    # TARGET_BUCKET_NAME=recovery-bucket-89898989
    
    # initialise aws cli
    # aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID;
    # aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY;
    # aws configure set default.region $REGION;
    
    # get current epoch time [6 digits]
    TIME_NOW=$(date +%s)
    
    # get all files from Source Bucket
    aws s3 sync s3://$SOURCE_BUCKET_NAME .
    # zip all files in Current Folder
    zip -r $TIME_NOW.zip terraform.tfstate
    # upload zip file to Target Bucket
    aws s3 cp  $TIME_NOW.zip s3://$TARGET_BUCKET_NAME
else
    raise error "Error copying files to s3 bucket"
fi



