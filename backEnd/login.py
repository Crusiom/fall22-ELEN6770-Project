import json
import boto3

def lambda_handler(event, context):
    
    email = event['email']
    pwd = event['pwd']
    
    statusCode = 200
    
    try:
        temp = lookup_data({'email': email})
    except Exception as e:
        temp = None
    if temp == None or temp['pwd'] != str(pwd):
        ret = "Login Failed..."
        statusCode = 403
    else:
        ret = temp
    return {
        'statusCode': statusCode,
        'body': ret
    }


def lookup_data(key, db=None, table='6770User'):
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