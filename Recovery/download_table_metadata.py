import boto3
import json
import sys
import os

SOURCE_AWS_ACCESS_KEY_ID = os.environ["SOURCE_AWS_ACCESS_KEY_ID"]
SOURCE_AWS_SECRET_ACCESS_KEY = os.environ["SOURCE_AWS_SECRET_ACCESS_KEY"]
# TABLE_NAME = os.environ["TABLE_NAME"]
TABLE_NAME = sys.argv[1]
REGION = os.getenv("REGION", "us-east-1")
print("TABLE_NAME is ", TABLE_NAME)

session = boto3.Session(
    aws_access_key_id=SOURCE_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=SOURCE_AWS_SECRET_ACCESS_KEY,
)

client = boto3.client("dynamodb")
source_table_meta_data = client.describe_table(TableName=TABLE_NAME)

del source_table_meta_data["Table"]["TableArn"]
del source_table_meta_data["Table"]["TableId"]
del source_table_meta_data["Table"]["TableSizeBytes"]
del source_table_meta_data["Table"]["CreationDateTime"]
del source_table_meta_data["Table"]["ItemCount"]
del source_table_meta_data["Table"]["TableStatus"]
del source_table_meta_data["Table"]["ProvisionedThroughput"]["NumberOfDecreasesToday"]

json_object = json.dumps(source_table_meta_data["Table"], indent=4, cls=DecimalEncoder)
print(json_object)
