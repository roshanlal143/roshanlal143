import boto3
# to create a bucket
client = boto3.client('s3')
resp = client.create_bucket(
    ACL='private',
    Bucket='094asefdasdf',
    CreateBucketConfiguration={
        'LocationConstraint' : 'ap-south-1'
    },
)

# to upload a file into the bucket
s3_upload = boto3.resource('s3')
s3_upload.meta.client.upload_file('C:\\New folder\\AWS Tutorials\\demo.ppk' , 'tsiplc409' , 'demo.ppk')

# to delete file from the bucket
response = client.delete_object(
    Bucket='tsiplc409',
    Key='demo.ppk',
)

# to delete the bucket
response = client.delete_bucket(
    Bucket='094asefdasdf',
)