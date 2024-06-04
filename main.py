import requests
import settings 
from previous import react_to_previous
import gateway

# Set login for all requests
req = requests.Session()
req.headers.update({"Authorization":settings.token})

# react_to_previous(req);
gateway.react(req);
