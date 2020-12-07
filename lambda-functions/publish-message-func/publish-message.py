import os
import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('sns', 'us-west-2')

    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            try:
                client.publish(
                    TopicArn=os.environ['TopicName'],
                    Message='An ordered just created successfully!',
                    Subject='A new order is created.'
                )

                response = {
                    'statusCode': 200,
                    'body': {
                        'message': 'Sending message successfully.'
                    }
                }

                return response
            except Exception as e:
                raise e
