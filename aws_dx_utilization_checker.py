import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')
directconnect = boto3.client('directconnect')

# Set period for the last 7 days
end_time = datetime.now()
start_time = end_time - timedelta(days=30)

# List all Direct Connect connections
dx_connections = directconnect.describe_connections()['connections']

for connection in dx_connections:
    connection_id = connection['connectionId']
    print(f"Checking metrics for Direct Connect ID: {connection_id}")

    for metric_name in ['DataInRate', 'DataOutRate']:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/DX',
            MetricName=metric_name,
            Dimensions=[{'Name': 'ConnectionId', 'Value': connection_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=3600,
            Statistics=['Average']
        )

        if response['Datapoints']:
            average = sum(d['Average'] for d in response['Datapoints']) / len(response['Datapoints'])
            print(f" - {metric_name} average: {average} Mbps")
        else:
            print(f" - {metric_name} has no data. This connection might not be in use.")
