import json
import boto3
import os
from datetime import datetime

client = boto3.client('cognito-idp')
user_pool_id=os.environ["USER_POOL_ID"]
cognito_data = []


try:
    group_names=fetch_cognito_groups()
    
    for group_name in group_names:
        users = list_users_in_group(group_name)
        params={"group_name":group_name,"users":users}
        print(params)
        cognito_data.append(params)
    
    full_path = './BackupFolder/cognito_backup/'    
    file_name = "cognito_backup.json"
    completePath = os. path. join(full_path, file_name)
    file = open(completePath, "w+")
    json_object = json.dumps(cognito_data, indent=4, default=json_serial)
    file.write(json_object)
    file.close()

except Exception as e:
    print(f"Internal Exception {e}!")
        
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type not serializable")

def fetch_cognito_groups():
    group_names=[]
    groups=client.list_groups(
        UserPoolId=user_pool_id,
    )["Groups"]
    for group in groups:
        group_names.append(group["GroupName"])
    print(group_names)
    return group_names

def list_users_in_group(group_name):
    response=client.list_users_in_group(
            UserPoolId=user_pool_id,
            GroupName=group_name,
            Limit=50
        )["Users"]
    return response
    
