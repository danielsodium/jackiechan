import requests
import json
import time
import urllib.parse
import websocket

# Params
token = ''
emoji = '🫃'
operation = ''
channel = ''

# Set login for all requests
req = requests.Session()
req.headers.update({"Authorization":token})

# Inital login request to get 50 messages
url = 'https://discord.com/api/v9/channels/{channel}/messages'.format(channel=channel)
x = req.get(url, headers={"Authorization":token})
response = json.loads(x.text)

# Set necessary strings
emoji = urllib.parse.quote(emoji, safe='')
delurl = 'https://discord.com/api/v9/channels/{channel}/messages/{id}/reactions/{emoji}/%40me?location=Message&burst=false'
posturl = 'https://discord.com/api/v9/channels/{channel}/messages/{id}/reactions/{emoji}/%40me?location=Message&type=0'

'''
# React to last 50 messages sent by user x
for msg in response:
    if (msg['author']['username'] == "cool_beans_bro"):
        if (operation == 'delete'):
            url = delurl.format(channel=msg['channel_id'], id=msg['id'], emoji=emoji)
            react = req.delete(url);
            time.sleep(0.5);
        else:
            url = posturl.format(channel=msg['channel_id'], id=msg['id'], emoji=emoji)
            react = req.put(url)
            time.sleep(0.5);

'''
# Websocket payload to login
loginpayload = ('{"op":2,"d":{"token":"'+token+'","capabilities":30717,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0","browser_version":"126.0","os_version":"","referrer":"","referring_domain":"","referrer_current":"https://discord.com/","referring_domain_current":"discord.com","release_channel":"stable","client_build_number":298544,"client_event_source":null,"design_id":0},"presence":{"status":"unknown","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_versions":{}}}}')

# Watch incoming messages thru websocket

def on_message(ws, message):
    msg = json.loads(message);
    if (msg['d']['author']['username'] == 'cool_beans_bro'):
        url = posturl.format(channel=msg['d']['channel_id'], id=msg['d']['id'], emoji=emoji)
        react = req.put(url)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    ws.send(loginpayload)
    # payload to select channel
    ws.send('{"op":37,"d":{"subscriptions":{"{'+channel+'}":{"typing":true,"threads":true,"activities":true,"members":[],"member_updates":false,"channels":{},"thread_member_lists":[]}}}}')
    
ws = websocket.WebSocketApp("wss://gateway.discord.gg", on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()  
