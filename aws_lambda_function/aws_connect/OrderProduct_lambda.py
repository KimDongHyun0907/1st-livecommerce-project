import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('connect_data')

def lambda_handler(event, context):
    realnum=event['Details']['ContactData']['CustomerEndpoint']['Address']
    realnum_key=realnum[-4:]
    
    info=table.get_item(Key={'phonenum': realnum_key})
    name=info['Item']['name']
    orderproduct = info['Item']['orderproduct']
    msg = str()
    
    for i in orderproduct:
        msg+=f'''{i} {orderproduct[i]}개 \n '''
    
    result = {
        "name":name,
        "msg":msg
    }
    
    return result
