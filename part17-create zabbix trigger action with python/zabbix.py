import requests
import json

# Zabbix API URL
url = "http://192.168.1.199/zabbix/api_jsonrpc.php"

# Zabbix API credentials
username = "Admin"
password = "zabbix"

# Zabbix item key for memory utilization
#item_key = "last(vm.memory.utilization)"

# Trigger expression for memory utilization
trigger_expression = "avg(/Zabbix server/vm.memory.utilization,4m)>80"

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
trigger_payload = {
    "jsonrpc": "2.0",
    "method": "trigger.create",
    "params": [
        {
        # Trigger name and description can be customized as per your requirements.
        # Here, we are using a generic name and description.
        # You can also set other trigger parameters such as severity, priority, etc.
        # For more details, refer to the Zabbix API documentation.
        "priority":"2",
        "description": "high memory utilization {HOST.NAME}",
        "expression": trigger_expression
        # Host ID and item ID can be obtained from the Zabbix web interface or API.
        # Here, we are assuming that the host and item already exist in Zabbix.
        
   
             
    },
    ],
    "auth": auth_token,
    "id": 52882
}

# Create a trigger for memory utilization item using the Zabbix API
response = requests.post(url, data=json.dumps(trigger_payload), headers=headers)
print(response.json())


#Note: Replace `your_zabbix_server`, `your_username`, `your_password`, `system.memory.util[,used]`, `your_host_id` and #`your_item_id` with your actual values.









