import json
import boto3

def lambda_handler(event, context):
    
    group = event['group']
    email = event['email']
    action = event['action']
    
    if action == 'kick':
        delete_item({'group' : group, 'email': email})
    elif action == 'mute':
        update_item({'email': email, 'group' : group}, 'mute')
    elif action == 'active':
        update_item({'email': email, 'group' : group}, 'active')
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

def delete_item(key, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    response = table.delete_item(Key=key)
    return response
        
def update_item(key, feature, db=None, table='6770Member'):
    if not db:
        db = boto3.resource('dynamodb')
    table = db.Table(table)
    # change student location
    response = table.update_item(
        Key=key,
        UpdateExpression="set #feature=:f",
        ExpressionAttributeValues={
            ':f': feature
        },
        ExpressionAttributeNames={
            "#feature": "status"
        },
        ReturnValues="UPDATED_NEW"
    )
    print(response)
    return response