import boto3
import json
import os

# tables = os.environ["STATE_LOCK_TABLE_NAME"].split(",")
tables = "restore-table,terraform_state".split(",")
# REGION = os.environ["REGION"]
REGION = os.getenv("REGION", "us-east-1")
# REGION = "us-east-1"

for table in tables:
    file_name = "./BackupFolder/" + table + ".json"
    file = open(file_name, "w+")
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    table = dynamodb.Table(table)
    response = table.scan()  # Download Dynamodb Table Contents
    json_object = json.dumps(response["Items"], indent=4)
    file.write(json_object)
    file.close()
