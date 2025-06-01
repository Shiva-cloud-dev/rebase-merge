import boto4

# Initialize S3 client
s3 = boto3.client('s3')

# 1. List all S3 buckets
response = s3.list_buckets()
print("list of S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")
