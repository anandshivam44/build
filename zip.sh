# FUNCTION_BUCKET_NAME=function-bucket-name-575859
# # aws s3 mb s3://$FUNCTION_BUCKET_NAME
# FUNCTION_FILE_NAME=LambdaFunction.zip

# pip3 install --target ./package requests
# cd package
# zip -r ../$FUNCTION_FILE_NAME .
# cd ..
# zip -g $FUNCTION_FILE_NAME index.py

# aws s3 cp $FUNCTION_FILE_NAME s3://$FUNCTION_BUCKET_NAME
