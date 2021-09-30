# import boto3
# import os

# def handler(event, context):
#     client = boto3.client("codepipeline")
#     response = client.start_pipeline_execution(name=os.getenv("BACKUP_PIPELINE_NAME"))
#     print(f"CodePipeline Response : {response}")
