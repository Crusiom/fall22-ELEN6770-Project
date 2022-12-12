import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    
    group = event['group']
    
    statusCode = 200
    ret = "Get all member successfully!"
    
    try:
        info = lookup_data(group)
    except Exception as e:
        info = e
        statusCode = 404
        ret = "Get all member failed!"
    
    
    
    return {
        'statusCode': statusCode,
        'body': info
    }
    
def lookup_data(key, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    scan_kwargs = {
        'FilterExpression': Key('group').eq(key)
    }
    try:
        response = table.scan(**scan_kwargs)
    except ClientError as e:
        print('Error', e.response['Error']['Message'])
    else:
        return response["Items"]