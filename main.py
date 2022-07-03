import discord
import requests
from queue import Queue
import time
from Alive import Alive
from threading import Timer

prevlength = 0
exponent18 = 10 ** -18
amount = 0
prevTotalSupply = 0
currentTotalSupply = 0
threshold = 1
discordnoti  = 0

async def sendMessage(message):
  await discord.utils.get(client.get_all_channels(),name='general').send(message)

async def SayHello(discordnoti, message):
  await sendMessage(f'Kuchh to chal')
  discordnoti+=1
  print(discordnoti)
  Timer(1.0, await SayHello(discordnoti, message)).start()

async def sectimer(message):
  while True:
    if message.content.startswith('stop'):
      return
    await sendMessage(f'sleep attempt')
    time.sleep(5)
  

def totalSupply(data):
  for i in range(0,len(data[0]['children'])):
    for j in range(0,len(data[0]['children'][i])):
      if "name" in data[0]['children'][i] and data[0]['children'][i]['name'] == "totalSupply":
        return float(data[0]['children'][i]['value'])*exponent18
  return 0

def compareTotalSupply(prevTotalSupply, currentTotalSupply,threshold):
  if abs(prevTotalSupply - currentTotalSupply) > threshold :
    return currentTotalSupply - prevTotalSupply
  else:
    return 0
  
def getBuy(prevlength):

  #extracting hash and buy details
  URL1="https://api.better-call.dev/v1/contract/hangzhou2net/KT1Mdk7TfHjbwb2ciTTsySj9gV9W9uc7HxCu/operations"
  
  r = requests.get(url=URL1)
  data = r.json()
  length = (len(data["operations"])) - prevlength
  prevlength = len(data["operations"])
  
  amount = 0
  for i in range(0,length) :
    hash=data['operations'][i]['hash']
    if "entrypoint" in data['operations'][i] and data['operations'][i]['entrypoint'] == "buy":
      amount = int(data['operations'][i-1]['parameters'][0]['children'][2]['value']) * exponent18
      print("Hash : " + str(hash),'\n',"Amount : " +str(amount))

def getTotalSupply():
  #extracting totalSupply
  URL2 = "https://api.better-call.dev/v1/contract/hangzhou2net/KT1K2PdgMbMuNSgTWYsTcoa6Du4KeJNeVC9U/storage"
  
  r = requests.get(url=URL2)
  data = r.json()
  supply = totalSupply(data)
  print("Current totalSupply : ", supply)
  return supply
  
getBuy(prevlength)

currentTotalSupply = getTotalSupply()
prevTotalSupply = currentTotalSupply

compareTotalSupply(prevTotalSupply, currentTotalSupply,threshold)

client = discord.Client()


@client.event
async def on_ready():
  print(f'you have logged in')
  channel = discord.utils.get(client.get_all_channels(),name='general')
  #await client.get_channel(channel.id).send(SayHello())


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('gintu'):
    await message.channel.send('bhopali')

  if message.content.startswith('start'):
    # await message.channel.send(await SayHello(discordnoti, message))
    await message.channel.send(await sectimer(message))

  if message.content.startswith('difference'):
    await message.channel.send('The is:'   + str(compareTotalSupply(prevTotalSupply, currentTotalSupply,threshold)))

Alive()

#bot token to be added
 
  
  #temp = compareTotalSupply(prevTotalSupply, currentTotalSupply,threshold)
  #prevTotalSupply = currentTotalSupply
  # timestamp=data['operations'][i]['timestamp']   #URL2="https://api.hangzhou2net.tzkt.io/v1/operations/"+hash
    # r2=requests.get(url=URL2)
    # data2=r2.json()
    # print(data2[i]['amount'])
  # oozYCzfzu5Ri9FeXK6KUiMq5dsYCRQktpbtkgkyCocr5bbyxG8W

  #if message.content.startswith(''):
    # await message.channel.send(f 'The current price of (message.content) is:   (getCryptoPrices (message.content. Lower ())) USD')
