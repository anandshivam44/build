import boto3
import json
import os
tables=[]
for i in range(10): #BACKUP_TABLE_NAME_1
    TABLE_NAME="BACKUP_TABLE_NAME_"+str(i)
    if os.environ[TABLE_NAME]!='NULL':
        tables.append(os.environ[TABLE_NAME])

REGION = os.getenv("REGION", "us-east-1")

for table in tables:
    file_name = "./BackupFolder/" + table + ".json"
    file = open(file_name, "w+")
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    table = dynamodb.Table(table)
    response = table.scan()  # Download Dynamodb Table Contents
    json_object = json.dumps(response["Items"], indent=4)
    file.write(json_object)
    file.close()
