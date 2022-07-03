import discord
import requests
from queue import Queue
import time
from Alive import Alive
from threading import Timer

last_time = [0]


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
    await sendMessage(getBuy(last_time))
    time.sleep(5)
  
  
def getBuy(last_time):
  if len(last_time)>5:
    t = last_time[-1]
    temp = [t]
    last_time[:]=temp[:]
  URL1="https://api.arbiscan.io/api?module=account&action=tokentx&contractaddress=0x539bdE0d7Dbd336b79148AA742883198BBF60342&page=1&offset=100&sort=desc&apikey=WMXSRXC98X444KH6PR1ZZNWARHH2RX8SBX"
  r = requests.get(url=URL1)
  data = r.json()
  results = data['result']
  # print(last_time)
  # print("++++++++++++++++++++++++")
  temp=[]
  for x in results:
      if(int(x['value']) > 1 * 10**18)and(int(x['timeStamp'])>last_time[-1]):
          temp.append(x['value']+x['hash'])
  last_time.append(int(results[0]['timeStamp']))
  print(last_time)
  print("----------------")
  return(temp)
 
getBuy(last_time)

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

# bot token to be added
 
