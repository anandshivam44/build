# Terraform-backend state backup and dynamodb backup pipeline
Deploys a cloudformation stack using cloudformation template to create an AWS codebuild project. This codebuild project will backup your Terraform backend state from SOURCE_BUCKET_NAME to TARGET_BUCKET_NAME

#### Prerequisites:
 - Terraform Backend configured with statelock in dynamodb table and state stored in SOURCE_BUCKET_NAME
 - TARGET_BUCKET_NAME that stores backup

#### Create Stack in cloudformation
Pass necessary parameters
 - DynamodbTableName
 - Region
 - SourceGihubRepoUrl: github url that contains build information and build commands
 - SourceBucketName
 - DestinationBucketName
```bash
aws cloudformation create-stack  --stack-name test-stack-name-2  \
--template-body file://cnf-codebuild.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--parameters  \
ParameterKey=DynamodbTableName,ParameterValue=terraform_state \
ParameterKey=Region,ParameterValue=us-east-1 \
ParameterKey=SourceGihubRepoUrl,ParameterValue=https://github.com/anandshivam44/build \
ParameterKey=SourceBucketName,ParameterValue=shivam-terraform-state-backend-1212121 \
ParameterKey=DestinationBucketName,ParameterValue=recovery-bucket-89898989

```
 Once you run this command. What happens next is cloudformation will 
 1. Create role and policy for cloudbuild project
 2. Create a cloudbuild project
 3. Attach role to cloudbuild so that cloudbuild can write logs to Cloud Formation and read write s3 buckets

 When build is triggered, 
 1. The build docker container will pull `terraform.state` file from `SOURCE_BUCKET_NAME` 
 2. Archive `terraform.state` using zip cli tool
 3. Push zip file to TARGET_BUCKET_NAME

#### Important Files
 - `cnf-codebuil.yaml` is cloudformatoion template
 - `buildspec.yaml` contains build information for codebuild
 - `backup.sh` contains shell coammands to will runn inside codebuild container
 - `read_state.py` this file is invoked by `backup.sh`. This python script waits untill there is no state lock and only then backup will start.

___
# Recovery
## Recover dynamodb from JSON file

###### How it works
We have dynamodb downloaded as JSON files. Now to replicate dynamodb from Source AWS account to Target AWS Account, first step is creating database. Download meta-data of dynamodb database from source account in `download_table_metadata` and use this to create database in Target account using AWS CLI

```bash
cd Recovery
# add env variables for python script to pull data from source account
export SOURCE_AWS_ACCESS_KEY_ID=[xxxxxxxxxxxxxx]
export SOURCE_AWS_SECRET_ACCESS_KEY=[xxxxxxxxxxxxxx]


```
#### Create database with exact meta-data/specifications
```bash
# assuming you have already configured aws cli for Target Account using "aws configure"

# pass the names of all databases as arguments
# sh create_databases.sh database-name-1 database-name-2 database-name-3 ... 
sh create_databases.sh database-name-1
```
#### Download restore zip file
```bash
aws s3 cp s3://bucket/file.zip .
unzip file.zip
```
#### Restore the values from .json to database
```bash
# Add multiple database as args to restore multiple databases
# python3 RestoreDatabase.py terraform_state database-name-1 database-name-2 database-name-3 ..

python3 RestoreDatabase.py terraform_state 
```

