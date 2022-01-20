from smartapi import SmartWebSocket, SmartConnect
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_CODE=os.getenv('Client_ID')
PASSWORD=os.getenv('Password')
API_KEY=os.getenv('API_key')

obj=SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_CODE,PASSWORD)
FEED_TOKEN = obj.getfeedToken() 

token="nse_cm|26009&nse_cm|26000"  
task="mw"

ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

def on_message(ws, message):
    print("Ticks: {}".format(message))
    
def on_open(ws):
    print("on open")
    ss.subscribe(task,token)
    
def on_error(ws, error):
    print(error)
    
def on_close(ws):
    print("Close")


ss._on_open = on_open
ss._on_message = on_message
ss._on_error = on_error
ss._on_close = on_close

ss.connect()