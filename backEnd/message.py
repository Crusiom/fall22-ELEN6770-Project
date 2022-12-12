import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    
    group = event['group']
    email = event['email']
    
    ret = None
    statusCode = 200
    
    try:
        member = lookup_data({"group": group, "email": email})
    except Exception as e:
        member = None
        ret = "You did not join this group..."
        statusCode = 403
    
    status = None
    
    if member != None:
        try:
            message = lookup_data_message(group)
            message.sort(key=getTime)
            ret = message
        except Exception as e:
            ret = "Find message failed..."

    return {
        'statusCode': statusCode,
        'body': ret,
        'status': member['status']
    }

def lookup_data(key, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    try:
        response = table.get_item(Key=key)
    except ClientError as e:
        print('Error', e.response['Error']['Message'])
    else:
        return response['Item']

def lookup_data_message(key, db=None, table='6770Message'):
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
        return response['Items']
        
def getTime(element):
    return eval(element['time'])