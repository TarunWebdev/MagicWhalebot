import requests
import re

prevId=0
# Buy notification
def data(prevId):
  URL1="https://api.tzkt.io/v1/accounts/KT1GRSvLoikDsXujKgZPsGLX8k8VvR2Tq95b/operations?entrypoint=transfer&limit=100"
  print('hi')
  r = requests.get(url=URL1)
  data = r.json()
  for i in range(0,100) :
    newId=data[i]['id']
    if prevId<newId :
      if 'to' in data[i]['parameter']['value']: 
          
        if 'from' in data[i]['parameter']['value']: 
            
          if data[i]['parameter']['value']['from'].startswith('KT1') : 
            if  data[i]['parameter']['value']['to'].startswith('tz1'):
          # print(i)
          # print(data[i]['sender']['address'])
              if 'alias' in data[i]['sender'] and 'farm' not in data[i]['sender']['alias'] and 'LP' not in data[i]['sender']['alias'] :
            # print(i)
                print(data[i]['sender']['alias'])
                print(data[i]['hash'])
                print(data[i]['initiator']['address'])
                
                amt =int(data[i]['parameter']['value']['value'])*(10**(-18))
                print(amt)
              # if 'value' in data[i]['parameter']['value']:
              #   print((data[i]['parameter']['value']['value']*(10**(-18))
    # if data[i]['sender']['address']!=data[i][value]['from']
    #agr to-> starts with 'KT' and sender starts with 'tz' and KT alias is not null->Alias mein farm h and swap ya LP nhi h ->amount =>300 -> Print krdo transaction hash
  prevId=data[0]['id']
  return prevId

  

prevId=data(prevId)
data(prevId)
print('this is prev Id out '+str(prevId))   
data(prevId)