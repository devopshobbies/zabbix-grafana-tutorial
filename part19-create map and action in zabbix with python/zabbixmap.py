import requests
import json

# Zabbix API URL
url = "http://192.168.1.199/zabbix/api_jsonrpc.php"

# Zabbix API credentials
username = "Admin"
password = "zabbix"

# Zabbix API request headers
headers = {"Content-Type": "application/json-rpc"}

# Zabbix API request payload for authentication
auth_payload = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": username,
        "password": password
    },
    "id": 1
}


# Authenticate with the Zabbix API and get the authentication token
response = requests.post(url, data=json.dumps(auth_payload), headers=headers)
auth_token = response.json()["result"]
print(response.json())

# Zabbix API request payload for creating a trigger for memory utilization item
zabbixmap_payload = {
           "jsonrpc": "2.0",
           "method": "map.create",
           "params": {
               "name": "Iran",
               "width": 600,
               "height": 600
           },
           "auth": auth_token,
           "id": 1
       }

# Create a trigger for memory utilization item using the Zabbix API
response = requests.post(url, data=json.dumps(zabbixmap_payload), headers=headers)
print(response.json())












