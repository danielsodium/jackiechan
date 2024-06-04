import json
import time
import websocket
import settings
import urllib.parse
import payload

posturl = 'https://discord.com/api/v9/channels/{channel}/messages/{id}/reactions/{emoji}/%40me?location=Message&type=0'
def react(req):
    def on_message(ws, message):
        msg = json.loads(message);
        if (msg['t'] == "MESSAGE_CREATE"):
            # filter by author channel etc here
            url = posturl.format(channel=msg['d']['channel_id'], id=msg['d']['id'], emoji=urllib.parse.quote(settings.emoji, safe=''))
            react = req.put(url)

    def on_error(ws, error):
        print(error)

    def on_close(ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(ws):
        print("Created Gateway")

        # Websocket payload to login
        ws.send(payload.login)
        time.sleep(1)
        ws.send(payload.guild)
        
    ws = websocket.WebSocketApp("wss://gateway.discord.gg", on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever(ping_interval=30, ping_payload=payload.ping)
