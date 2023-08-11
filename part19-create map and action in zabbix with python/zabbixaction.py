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
           "method": "action.create",
           "auth": auth_token,
           "id": 1,
           "params": {
               "name": "Trigger action 2 ",
               "eventsource": 0,
               "esc_period": "30m",
               "filter": {
                   "evaltype": 0,
                   "conditions": [
                       {
                           "conditiontype": "1",
                           "operator": "0",
                           "value": "10084"
                       },
                   ]
               },
               "operations": [
                   {
                       "operationtype": "0",
                       "esc_step_from": 1,
                       "esc_step_to": 1,
                       "opmessage_grp": [
                           {
                               "usrgrpid": "7"
                           }
                       ],
                       "opmessage": {
                           "default_msg": "1",
                           "mediatypeid": "1"
                       }
                   },
               ],
               "recovery_operations": [
                   {
                       "operationtype": "11",
                       "opmessage": {
                           "default_msg": 1
                       }
                   }
               ],
               "update_operations": [
                   {
                       "operationtype": "12",
                       "opmessage": {
                           "default_msg": 0,
                           "message": "Custom update operation message body",
                           "subject": "Custom update operation message subject"
                       }
                   }
               ]
           },
           "id": 1
       }
# Create a trigger for memory utilization item using the Zabbix API
response = requests.post(url, data=json.dumps(zabbixmap_payload), headers=headers)
print(response.json())












