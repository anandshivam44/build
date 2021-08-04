import boto3
import os

STATE_LOCK_TABLE_NAME =os.environ['STATE_LOCK_TABLE_NAME']
REGION =os.environ['REGION']

# session = boto3.Session(
#     aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
#     aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
# )
# dynamodb = session.resource("dynamodb", region_name=REGION)

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(STATE_LOCK_TABLE_NAME)


terraform_state_lock = True  # assume there is a 'terraform apply' command running


while terraform_state_lock == True: # as long as 'apply command is running' while loop will block the thread

    response = table.scan()  # Download Dynamodb Table Contents

    if len(response["Items"]) == 0:
        raise ValueError("There is no state definition in dynamodb. You sure eveything is fine??? If this code was not supposed to throw an error, then this python file needs editing")
    for state in response["Items"]:  # Iterate through each states
        terraform_state_lock = 'Info' in state

else: # release this while loop when there is no state lock/ no 
    print("StartBackup")
