import boto3
import json
import os
from decimal import Decimal

REGION = os.getenv("REGION")
dynamodb = boto3.resource("dynamodb", region_name=REGION)
tables = []

# print("Table Name", os.environ["BACKUP_TABLE_NAME"])
# print(type(os.environ["BACKUP_TABLE_NAME"]))

for i in range(5):  # BACKUP_TABLE_NAME_1
    TABLE_NAME = "BACKUP_TABLE_NAME_" + str(i)
    if os.environ[TABLE_NAME] != "NULL":
        print("Backing up TABLE_NAME=", os.environ[TABLE_NAME])
        tables.append(os.environ[TABLE_NAME])

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

for table in tables:
    file_name = "./BackupFolder/" + table + ".json"
    file = open(file_name, "w+")
    table = dynamodb.Table(table)
    response = table.scan()  # Backup Dynamodb Table Contents
    json_object = json.dumps(response["Items"], indent=4, default=default)
    file.write(json_object)
    file.close()
