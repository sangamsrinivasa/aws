import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='your-region')
    dynamodb = boto3.client('dynamodb', region_name='your-region')
    
    response = ec2.run_instances(
        ImageId='ami-xxxxxx',  # Replace with your AMI ID
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='your-key-pair',  # Replace with your key pair name
        SubnetId='subnet-xxxxxx',  # Replace with your subnet ID
        SecurityGroupIds=['sg-xxxxxx']  # Replace with your security group ID
    )
    instance_id = response['Instances'][0]['InstanceId']
    
    dynamodb.put_item(
        TableName='EC2Instances',
        Item={'InstanceId': {'S': instance_id}}
    )
    return instance_id

