import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Define the threshold for considering a bucket as stale (e.g., 30 days)
    threshold_days = 30
    
    # Get list of all S3 buckets
    response = s3.list_buckets()
    
    # Iterate over each bucket
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        # Get last access time for the bucket
        try:
            response = s3.get_bucket_tagging(Bucket=bucket_name)
            for tag in response['TagSet']:
                if tag['Key'] == 'LastAccessTime':
                    last_access_time = datetime.strptime(tag['Value'], '%Y-%m-%d %H:%M:%S.%f')
                    break
        except Exception as e:
            print(f"Error getting tags for bucket {bucket_name}: {e}")
            continue
        
        # Check if the bucket is stale
        if datetime.now() - last_access_time > timedelta(days=threshold_days):
            # Move the bucket to Glacier storage class
            try:
                s3.put_bucket_lifecycle_configuration(
                    Bucket=bucket_name,
                    LifecycleConfiguration={
                        'Rules': [
                            {
                                'Expiration': {'Days': 0},
                                'Filter': {'Prefix': ''},
                                'ID': 'MoveToGlacier',
                                'Status': 'Enabled',
                                'Transitions': [
                                    {
                                        'Days': 0,
                                        'StorageClass': 'GLACIER'
                                    }
                                ]
                            }
                        ]
                    }
                )
                print(f"Bucket {bucket_name} moved to Glacier storage class.")
            except Exception as e:
                print(f"Error moving bucket {bucket_name} to Glacier: {e}")
                continue
    
    return {
        'statusCode': 200,
        'body': 'S3 bucket archival completed.'
    }

