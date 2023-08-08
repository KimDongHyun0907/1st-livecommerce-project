import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('buy_product')

rr=table.scan()
temp=[]
buy_products=[]
for x in range(len(rr['Items'])):
    temp.append(rr['Items'][x]['date'])
    temp.append(rr['Items'][x]['name'])
    temp.append(str(rr['Items'][x]['count']))
    buy_products.append(temp)
    temp=[]

buy_products.sort()
    
dynamodb2 = boto3.resource('dynamodb')
table2 = dynamodb.Table('recommend_product')
ee=table2.scan()
#print(ee)
recommend_product={}
for i in range(len(ee['Items'])):
    recommend_product[ee['Items'][i]['name']]=[ee['Items'][i]['type'], int(ee['Items'][i]['age']), ee['Items'][i]['gender'], int(ee['Items'][i]['priority'])]

dynamodb3 = boto3.resource('dynamodb')
table3 = dynamodb.Table('onsale_info')
oo=table3.scan()
#print(oo)
onsale_info=[]
for i in range(len(oo['Items'])):
    temp=[]
    temp.append(oo['Items'][i]['date'])
    temp.append(int(oo['Items'][i]['start_time']))
    temp.append(int(oo['Items'][i]['end_time']))
    temp2=[]
    for j in oo['Items'][i]['product_percent']:
        temp2.append([j, oo['Items'][i]['product_percent'][j]])
    temp.append(temp2)
    onsale_info.append(temp)
print(onsale_info)

onsale_product=onsale_info[0][3]
product_msg=str()
percent_msg=str()
for product,percent in onsale_product:
    product_msg+=product+', \n'
    percent_msg+=product+' '+str(percent)+'% \n'

product_msg=product_msg[:len(product_msg)-3]
percent_msg=percent_msg[:len(percent_msg)-2]
    
def lambda_handler(event, context):
    print(event)
    slots=event['sessionState']['intent']['slots']
    intent=event['sessionState']['intent']['name']
    print(intent)
    print(slots)
    
    #print(buy_products2)
    
    if intent=='GuideIntent':
        if event['inputTranscript'].find('시간')!=-1:
            onsale_date=onsale_info[0][0]
            year,month,day=onsale_date.split('-')
            
            st=onsale_info[0][1]
            et=onsale_info[0][2]
            
            if st>12:
                st_msg='오후 '+str(st-12)
            elif st==12:
                st_msg='오후 '+str(12)
            else:
                st_msg='오전 '+str(st)
            
            if et>12:
                et_msg='오후 '+str(et-12) 
            elif et==12:
                et_msg='오후 '+str(12)
            else:
                et_msg='오전 '+str(et)
                
            response={
                "sessionState":{
                    "dialogAction":{
                        "type":"Close"
                    },
                    "intent":{
                        "name":intent,
                        "slots":slots,
                        "state":"Fulfilled"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f'''특가 시간은 {year}년 {month}월 {day}일 {st_msg}시부터 {et_msg}시입니다.'''
                    },
                    {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 구매목록 \n 2. 추천 상품 \n 3. 상담원 연결"
                    }
                ]
            }
        
        elif event['inputTranscript'].find('상품')!=-1:
            response={
                "sessionState":{
                    "dialogAction":{
                        "type":"Close"
                    },
                    "intent":{
                        "name":intent,
                        "slots":slots,
                        "state":"Fulfilled"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f'''이번 특가 상품은 \n{product_msg}입니다.'''
                    },
                    {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 구매목록 \n 2. 추천 상품 \n 3. 상담원 연결"
                    }
                ]
            }
        elif event['inputTranscript'].find('할인율')!=-1:
            response={
                "sessionState":{
                    "dialogAction":{
                        "type":"Close"
                    },
                    "intent":{
                        "name":intent,
                        "slots":slots,
                        "state":"Fulfilled"
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f'''{percent_msg}입니다.'''
                    },
                    {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 구매목록 \n 2. 추천 상품 \n 3. 상담원 연결"
                    }
                ]
            }
        
        else:
            response={
                "sessionState":{
                    "dialogAction":{
                        "slotToElicit": "SaleType",
                        "type": "ElicitSlot"
                    },
                    "intent":{
                        "name":intent,
                        "slots":slots
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": f'''네. 특가 서비스에 대해 어떤 내용이 궁금하신가요?\n 1. 특가 시간\n 2. 특가 상품\n 3. 특가 할인율'''
                    }
                ]
            }
    
    elif intent=='BuyCheckProduct':
        answer=str()
        for date, product,cnt in buy_products:
            year, month, day=date.split('-')
            tmp_answer=f'''{year}년 {month}월 {day}일\n{product}\n수량 {cnt}\n'''
            answer+='\n'+tmp_answer
            tmp_answer=str()
        
        
        response={
            "sessionState":{
                "dialogAction":{
                    "type":"Close"
                },
                "intent":{
                    "name":intent,
                    "slots":slots,
                    "state":"Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f'''구매 목록은 다음과 같습니다.\n{answer}입니다.'''
                },
                {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 특가 할인 \n 2. 추천 상품 \n 3. 상담원 연결"
                }
            ]
        }
    
    elif intent=='RecommendProduct':
        if slots['AgeType']==None and slots['GenderType']==None and slots['ProductKind']==None:
            response={
                "sessionState":{
                    "dialogAction":{
                        "slotToElicit": "ProductKind",
                        "type": "ElicitSlot"
                    },
                    "intent":{
                        "name":intent,
                        "slots":slots
                    }
                }
            }
        
        elif slots['ProductKind']!=None:
            if slots['AgeType']!=None:
                if slots['GenderType']!=None:
                    reco_product,reco_age,reco_gender=slots['ProductKind']['value']['originalValue'],slots['AgeType']['value']['originalValue'],slots['GenderType']['value']['originalValue']
                    reco_age=int(reco_age)-(int(reco_age)%10)
                    reco_gender=reco_gender[0]
                    key_list=list(recommend_product.keys())
                    reco_list=[]
                    
                    for i in key_list:
                        point=0
                        if recommend_product[i][0]==reco_product:
                            if reco_age==recommend_product[i][1]:
                                point+=1
                            if reco_gender==recommend_product[i][2]:
                                point+=1
                            reco_list.append((i,point,recommend_product[i][3]))
                    
                    reco_list=sorted(reco_list,key=lambda x:(-x[1],x[2]))
                    response={
                        "sessionState":{
                            "dialogAction":{
                                "type": "Close"
                            },
                            "intent":{
                                "name":intent,
                                "slots":slots,
                                "state":"Fulfilled"
                            }
                        },
                        "messages": [
                            {
                                "contentType": "PlainText",
                                "content": f'''추천 받은 상품은 {reco_list[0][0]}입니다.'''
                            },
                            {
                                "contentType": "PlainText",
                                "content": "추가로 필요하면 말씀해주세요 \n 1. 구매 목록 \n 2. 특가 할인 \n 3. 상담원 연결"
                            }
                        ]
                    }
                else:
                    response={
                        "sessionState":{
                            "dialogAction":{
                                "slotToElicit": "GenderType",
                                "type": "ElicitSlot"
                            },
                            "intent":{
                                "name":intent,
                                "slots":slots
                            }
                        }
                    }
            
            else:
                response={
                    "sessionState":{
                        "dialogAction":{
                            "slotToElicit": "AgeType",
                            "type": "ElicitSlot"
                        },
                        "intent":{
                            "name":intent,
                            "slots":slots
                        }
                    }
                }
    
    elif intent=='AgentConnect':
        response={
            "sessionState":{
                "dialogAction":{
                    "type":"Close"
                },
                "intent":{
                    "name":intent,
                    "slots":slots,
                    "state":"Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "상담원 및 ARS 연결은 다음 번호로 연결해주시기 바랍니다.\n0036512524000175\n온리원과 고객센터 상담원이 친절하게 답변드리겠습니다."
                },
                {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 구매 목록 \n 2. 특가 할인 \n 3. 추천 상품"
                }
            ]
        }

    else:
        response={
            "sessionState":{
                "dialogAction":{
                    "type":"Close"
                },
                "intent":{
                    "name":intent,
                    "slots":slots,
                    "state":"Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "챗봇의 기능은 [구매 목록, 특가 할인, 추천 상품, 상담원 연결]만 가능합니다."
                },
                {
                        "contentType": "PlainText",
                        "content": "추가로 필요하면 말씀해주세요 \n 1. 구매 목록 \n 2. 특가 할인 \n 3. 추천 상품 \n 4. 상담원 연결 "
                }
            ]
        }
        
    print(response)
    return response
