import boto3
import os

def handler(event, context):
    client = boto3.client("codebuild")
    PROJECT_NAME = os.getenv("PROJECT_NAME", "TerraformStateBackup")
    #response = client.start_build(projectName=PROJECT_NAME)
    response = codepipeline.start_pipeline_execution(
        name=os.getenv("BACKUP_PIPELINE_NAME")
    )
    print(f"CodePipeline Response : {response}")
