# #!/bin/bash

# python3 read_state.py

# echo "Start DynamoDB Backup"
# python3 download_dynamodb_tables.py
# echo "DynamoDB Backup Completed"
# # get current epoch time [6 digits]
# TIME_NOW=$(date +%s)
# echo $TIME_NOW
# # get all files from Source Bucket
# echo "Start Copy terraform.state file from s3"
# aws s3 sync s3://$SOURCE_BUCKET_NAME ./BackupFolder
# echo "Copy terraform.state file from s3 Completed"
# # zip all files in Current Folder
# cd BackupFolder
# zip -r  ../$TIME_NOW.zip .
# cd ..
# # upload zip file to Target Bucket
# echo "Upload zip file to s3 Starte"
# aws s3 cp  $TIME_NOW.zip s3://$TARGET_BUCKET_NAME
# echo "Upload zip file to s3 Completed"




