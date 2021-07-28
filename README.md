Terraform state backup

Run the Template
```
aws cloudformation deploy --template-file cnf-codebuild.yaml --stack-name <STACK_NAME> --debug
```

Required Environment Variables
 - STATE_LOCK_TABLE_NAME
 - REGION
 - SOURCE_BUCKET_NAME
 - TARGET_BUCKET_NAME

