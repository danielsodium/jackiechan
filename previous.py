import requests
import json
import time
import urllib.parse
import settings

def react_to_previous(req):
    # Inital login request to get 50 messages
    url = 'https://discord.com/api/v9/channels/{channel}/messages'.format(channel=settings.channel)
    x = req.get(url)
    response = json.loads(x.text)

    # Set necessary strings
    emoji = urllib.parse.quote(settings.emoji, safe='')
    delurl = 'https://discord.com/api/v9/channels/{channel}/messages/{id}/reactions/{emoji}/%40me?location=Message&burst=false'
    posturl = 'https://discord.com/api/v9/channels/{channel}/messages/{id}/reactions/{emoji}/%40me?location=Message&type=0'

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
