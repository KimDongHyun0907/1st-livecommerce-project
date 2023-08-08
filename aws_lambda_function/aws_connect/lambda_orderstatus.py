import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('connect_data')

def lambda_handler(event, context):
    print(event)
    realnum=event['Details']['ContactData']['CustomerEndpoint']['Address']
    realnum_key=realnum[-4:]
    
    info=table.get_item(Key={'phonenum': realnum_key})
    
    orderno = event['Details']['Parameters']['OrderNo'];
    ordercode=info['Item']['ordercode']
    
    isTrue=False
    _index=0
    for i in range(len(ordercode)):
        if orderno==ordercode[i][0]:
            _index=i
            isTrue=True
            break
    
    if isTrue:
        orderstatus=ordercode[_index][1]
        expecttime=ordercode[_index][2]
        result = {
            "orderstatus" : orderstatus,
            "expecttime" : expecttime
        }
    
        return result
    
    else:
        return False
