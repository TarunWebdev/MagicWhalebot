# Logic: Phele get all origination contract address -> fir filter our those jinke token pair ho ie. look for keywords jaise ki swap -> Address fetch kro -> fir add liquidity transaction deko -> Uske baad tz to KT hora h ye dekho -> uske 
prevId=0
def getData():
  URL1="https://api.tzkt.io/v1/accounts/tz1NbDzUQCcV2kp3wxdVHVSZEDeq2h97mweW/operations?type=origination&limit=300"
  r = requests.get(url=URL1)
  data = r.json()
  print(len(data))
  for i in range(0,len(data)) :
    if 'alias' in data[i]['originatedContract'] and ('Swap' in data[i]['originatedContract']['alias'] or 'swap' in data[i]['originatedContract']['alias'] ):
      print(data[i]['originatedContract']['address'])
      if(data[i]['originatedContract']['address']=='KT1VeNQa4mucRj36qAJ9rTzm4DTJKfemVaZT'):
        print("wohoooooo")
        
      URL2="https://api.tzkt.io/v1/accounts/"+data[i]['originatedContract']['address']+"/operations?entrypoint=add_liquidity"
      r1 = requests.get(url=URL2)
      data1 = r1.json()
      print(len(data1))
      for j in range(0 ,len(data1)):
        if data[j]['type']=='transaction' and 'parameter' in data1[j]:
          print(data1[j]['parameter']['value']['maxCashDeposited'])
      # parameter->value->maxdeposited


getData()