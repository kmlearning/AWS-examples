'''
Example for using a lambda function to write a file to s3

Ensure lambda function has role which allows for s3 write access
Can trigger function to run on events, schedule, etc via CloudWatch
'''


import boto3


def lambda_handler(event, context):
    string = 'Hello world'
    encoded_string = string.encode('utf-8')
    
    bucket_name = 'ld-test-km-lse-scraper'
    # top level folder should not have / at front
    file_path = 'test/hello.txt'

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    bucket.put_object(
        Key = path_name,
        Body = encoded_string
    )
    
    return {
        'statusCode': 200
    }
