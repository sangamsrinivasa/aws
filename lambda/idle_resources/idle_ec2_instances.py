#####################################
                                    #
Author: Srinivasreddy Sangam        #
CreateDate: 11 June 2024            #
Description: Identify EC2 instances #
             which are idle         #
#####################################

#import libraries
import boto3
import datetime

# Create AWS clients
ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwatch')

# Define the time period for checking CPU utilization
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(days=15)

# Specify the VPC ID if this function is targetted for a specific VPC
VPC_ID = 'vpc-xxxxxxxx'

def get_unused_instances():

    instances = ec2_client.describe_instances(Filters=[
        {
            'Name': 'vpc-id',
            'Values': [VPC_ID]
        }
    ])
    unused_instances = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            # Check only running instances
            if state != 'running':
                continue

            # Get CPU utilization for the past 15 days
            metrics = cloudwatch_client.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                StartTime=start_time,
                EndTime=end_time,
                Period=86400,  # 1 day intervals
                Statistics=['Average']
            )

            # Check if CPU utilization is consistently low
            if metrics['Datapoints']:
                avg_cpu_utilization = sum(point['Average'] for point in metrics['Datapoints']) / len(metrics['Datapoints'])
                if avg_cpu_utilization < 10:  # Assuming an instance is unused if CPU utilization is < 10%
                    unused_instances.append(instance_id)

    return unused_instances

def lambda_handler(event, context):
    unused_instances = get_unused_instances()
    if unused_instances:
        return {
            'statusCode': 200,
            'body': f"Unused EC2 instances: {', '.join(unused_instances)}"
        }
    else:
        return {
            'statusCode': 200,
            'body': "No unused EC2 instances found."
        }


