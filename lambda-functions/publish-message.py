import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('sns', 'us-west-2')

    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            try:
                client.publish(
                    TopicArn='arn:aws:sns:region:accountID:OrderTopic',
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
                raise 'Sending message fail.' + e
