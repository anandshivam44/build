from decimal import Decimal
import json
import boto3
import sys
dynamodb = boto3.resource("dynamodb")


def load_items(Items, DATABASE_NAME, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table(DATABASE_NAME)
    for item in Items:
        table.put_item(Item=item)


def pick_json_files(DATABASE_NAME):
    PATH_TO_FILE = DATABASE_NAME + ".json"
    with open(PATH_TO_FILE) as json_file:
        Items = json.load(json_file, parse_float=Decimal)
    load_items(Items, DATABASE_NAME)

''' check the number of arguments passed
    starting from index 1 contains the name of database
'''
n = len(sys.argv)
print(sys.argv)
for i in range(1, n):
    pick_json_files(sys.argv[i])
