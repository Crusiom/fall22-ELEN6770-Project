import json
import boto3

def lambda_handler(event, context):
    
    name = event['name']
    email = event['email']
    pwd = event['pwd']
    try:
        temp = lookup_data({'email':email})
    except Exception as e:
        temp = None
    
    ret = "This email is already registered..."
    statusCode = 403
    
    if temp == None:
        ret = insert_data([{
            'name':name,
            'email':email,
            'pwd':pwd
        }])
        if ret["ResponseMetadata"]["HTTPStatusCode"] == 200:
            ret = "Register successfully!"
            statusCode = 200
        
    return {
        'statusCode': statusCode,
        'body': ret
    }

def insert_data(data_list, db=None, table='6770User'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    # overwrite if the same index is provided
    for data in data_list:
        response = table.put_item(Item=data)
    print('@insert_data: response', response)
    return response


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

    # 1
    # insert_data(student)
    # 2
    # lookup_data({'uni': 'xx777'})
    # 3
    # update_item({'uni': 'xx777'}, 'Canada')
    # 4
    # delete_item({'uni': 'xx777'})