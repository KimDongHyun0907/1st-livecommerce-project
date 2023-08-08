import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('connect_data')

def lambda_handler(event, context):
    print(event)
    phonenum = event['Details']['Parameters']['PhoneNum'];
    if len(phonenum) == 11:
        realnum=event['Details']['ContactData']['CustomerEndpoint']['Address']
        
        if realnum[-8:]==phonenum[3:]:
            info=table.get_item(Key={'phonenum':phonenum[-4:]})
            print(info)
            print(info['Item']['name'])
            print(info['Item']['ordercode'])
            print(info['Item']['orderproduct'])
            
            name=info['Item']['name']
            
            result = {
                "phonenum": phonenum,
                "name": name
            }
            print(result)
            return result
        return False
        
    
    return False
