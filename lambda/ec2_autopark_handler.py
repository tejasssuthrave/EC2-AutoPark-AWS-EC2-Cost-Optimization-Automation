import boto3
import os

# AWS clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# Environment variable
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']


def get_instance_details(instances):
    details = []

    for instance in instances:
        name = "N/A"
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']

        details.append({
            "id": instance['InstanceId'],
            "name": name,
            "private_ip": instance.get('PrivateIpAddress', 'N/A'),
            "public_ip": instance.get('PublicIpAddress', 'N/A')
        })

    return details


def lambda_handler(event, context):
    action = event.get('action')

    if action not in ["start", "stop"]:
        return {"error": "Invalid action. Use start or stop"}

    # Fetch EC2 instances with AutoPark=true tag
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:AutoPark', 'Values': ['true']},
            {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
        ]
    )

    instances = []
    instance_ids = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
            instance_ids.append(instance['InstanceId'])

    if not instance_ids:
        return {"message": "No EC2 instances found with AutoPark=true"}

    # Perform action
    if action == "stop":
        ec2.stop_instances(InstanceIds=instance_ids)
        action_text = "STOPPED"
    else:
        ec2.start_instances(InstanceIds=instance_ids)
        action_text = "STARTED"

    # Fetch details for email
    instance_details = get_instance_details(instances)

    # Email message
    message = f"EC2 AutoPark Notification\n\nAction: {action_text}\n\n"

    for inst in instance_details:
        message += (
            f"Instance Name : {inst['name']}\n"
            f"Instance ID   : {inst['id']}\n"
            f"Private IP    : {inst['private_ip']}\n"
            f"Public IP     : {inst['public_ip']}\n"
            f"-----------------------------\n"
        )

    # Send SNS email
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f"EC2 Instance {action_text}",
        Message=message
    )

    return {
        "message": f"{action_text} instances successfully",
        "instances": instance_ids
    }
