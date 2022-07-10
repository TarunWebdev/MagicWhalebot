import discord
import requests
from queue import Queue
import time
from Alive import Alive
from threading import Timer

last_time = [0]


async def sendMessage(message):
  amount = str(round(message[0],2))
  wallet = message[1]
  txid = message[2]
  msg = str(amount)+ "$Magic transfered from wallet " + wallet + "\n\nArbiscan :" +txid
  embed=discord.Embed(title="MAGIC WHALE TRANSACTOIN", url=txid, description=msg, color=0x202225)
  await discord.utils.get(client.get_all_channels(),name='general').send(embed=embed)


async def sectimer(message):
  while True:
    if message.content.startswith('stop'):
      return
    result = getBuy(last_time)
    if len(result)>1:
      for item in result:
        await sendMessage(item)
      sendMessage('done')
    time.sleep(5)
  
def getBuy(last_time):
  if len(last_time)>10:
    t = last_time[-1]
    temp = [t]
    last_time[:]=temp[:]
  URL1="https://api.arbiscan.io/api?module=account&action=tokentx&contractaddress=0x539bdE0d7Dbd336b79148AA742883198BBF60342&page=1&offset=10&sort=desc&apikey=WMXSRXC98X444KH6PR1ZZNWARHH2RX8SBX"
  r = requests.get(url=URL1)
  data = r.json()
  results = data['result']
  temp=[]
  i=0
  for x in results:
      item=[]
      if(int(x['value']) > 1 * 10**18)and(int(x['timeStamp'])>last_time[-1]):
          val= int(x['value']) / (10**18)
          sender = x['from']
          hash = "https://arbiscan.io/tx/"+x['hash']
          item.append(val)
          item.append(sender)
          item.append(hash)
          temp.append(item)
  last_time.append(int(results[0]['timeStamp']))
  print(last_time)
  # print("----------------")
  return(temp)
 

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

  if message.content.startswith('start'):
    await message.channel.send(await sectimer(message))





Alive()

# bot token to be added

client.run("")
