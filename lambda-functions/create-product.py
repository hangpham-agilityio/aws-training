import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Product')

    data = json.loads(event['body'])
    table.put_item(
        Item={
            "product_id": data['product_id'],
            "name": data['name'],
            "price": data['price'],
            "quantity": data['quantity']
        })

    response = {
        "statusCode": 200,
        'body': json.dumps(data)
    }

    return response
