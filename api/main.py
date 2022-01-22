from smartapi import SmartWebSocket, SmartConnect
import os
from dotenv import load_dotenv
from weightageMove import weightageMove
from stockIndices import getData
import stockIndices

load_dotenv()

CLIENT_CODE=os.getenv('Client_ID')
PASSWORD=os.getenv('Password')
API_KEY=os.getenv('API_key')

obj=SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_CODE,PASSWORD)
FEED_TOKEN = obj.getfeedToken() 

# nifty = 26000 banknift = 26009

token="nse_cm|26000&nse_cm|26009"  
task="mw"

example = [{'e': 'nse_cm', 'ltp': '1955.20', 'ltq': '2', 'ltt': 'NA', 'name': 'sf', 'tk': '11483'}, {'c': '17757.00', 'cng': '-146.85', 'e': 'nse_cm', 'ltp': '17610.15', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.827', 'tk': '26000'}, {'c': '37850.85', 'cng': '-313.65', 'e': 'nse_cm', 'ltp': '37537.20', 'ltt': 'NA', 'name': 'sf', 'nc': '-00.8286', 'tk': '26009'}]

ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)

def on_message(ws, message):
    # stockIndObj = stockIndices.stockIndices()
    # stockIndObj.abc(message)
    # getData(message)
    # weightageMove()
    print(message)
    
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