from flask import Flask
from threading import Thread 

app = Flask('pyth')

@app.route('/')
def home():
  return 'Hello. The Crypto Bot is running YA YEET!'

def run():
  app.run(host='0.0.0.0',port=8000)

def Alive():
  t = Thread(target=run)
  t.start()