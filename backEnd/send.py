import json
import boto3
from boto3.dynamodb.conditions import Key
import time

def lambda_handler(event, context):
    
    time_value = str(time.time())
    group = event['group']
    email = event['email']
    id = event['email'] + "-" + time_value
    msg = event['msg']
    ret = None
    statusCode = 200
    name = "Danling Wei"
    
    try:
        member = lookup_data({"group": group, "email": email})
        print(member)
        name = member['name']
    except Exception as e:
        member = None
        ret = "You did not join this group..."
        statusCode = 403
    
    if member != None:
        ret = insert_data([{
            'name':name,
            'email':email,
            'id':id,
            'group':group,
            'msg':msg,
            'time': time_value
        }])
        if ret["ResponseMetadata"]["HTTPStatusCode"] == 200:
            ret = "Send message successfully!"
        else:
            statusCode = 403
            ret = "Send message failed..."
            
    return {
        'statusCode': statusCode,
        'body': ret
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

def insert_data(data_list, db=None, table='6770Message'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    # overwrite if the same index is provided
    for data in data_list:
        response = table.put_item(Item=data)
    print('@insert_data: response', response)
    return response