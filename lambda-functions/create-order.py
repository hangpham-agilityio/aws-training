import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Order')

    data = json.loads(event['body'])
    table.put_item(
        Item={
            "order_id": data['order_id'],
            "total_price": data['total_price'],
            "datetime": data['datetime']
        })

    response = {
        "statusCode": 201,
        'body': json.dumps(data)
    }

    return response
