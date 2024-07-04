import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='your-region')
    dynamodb = boto3.client('dynamodb', region_name='your-region')
    
    response = dynamodb.scan(
        TableName='EC2Instances'
    )
    
    if 'Items' in response and response['Items']:
        instance_id = response['Items'][0]['InstanceId']['S']
        
        ec2.terminate_instances(InstanceIds=[instance_id])
        
        dynamodb.delete_item(
            TableName='EC2Instances',
            Key={'InstanceId': {'S': instance_id}}
        )
    return response

