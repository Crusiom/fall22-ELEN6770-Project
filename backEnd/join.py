import json
import boto3
import time

def lambda_handler(event, context):
    
    email = event['email']
    name = event['name']
    group = event['group']
    gpwd = event['gpwd']
    
    try:
        ginfo = lookup_data({'group': group})
    except Exception as e:
        ginfo = None
        
    statusCode = 403
    ret = "Group Information Incorrect...!"
    
    if (ginfo != None):
        try:
            member = lookup_data_member({'group':group ,'email':email})
        except Exception as e:
            member = None
        if member == None and gpwd == ginfo['gpwd']:
            ret = insert_data([{
                'name': name,
                'group':group,
                'email': email,
                'status': 'active'
            }])
            if ret["ResponseMetadata"]["HTTPStatusCode"] == 200:
                statusCode = 200
                ret = "Join successfully!"
            else :
                ret = "Join Failed..."
        else:
            ret = "Join Failed: Password error OR You have already join"
    
    return {
        'statusCode': statusCode,
        'body': ret
    }

def insert_data(data_list, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    # overwrite if the same index is provided
    for data in data_list:
        response = table.put_item(Item=data)
    print('@insert_data: response', response)
    return response
    
def lookup_data(key, db=None, table='6770group'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    try:
        response = table.get_item(Key=key)
    except ClientError as e:
        print('Error', e.response['Error']['Message'])
    else:
        print(response['Item'])
        return response['Item']
        
def lookup_data_member(key, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    try:
        response = table.get_item(Key=key)
    except ClientError as e:
        print('Error', e.response['Error']['Message'])
    else:
        print(response['Item'])
        return response['Item']