from fastapi import FastAPI
import uvicorn
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import SSHException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import ReadTimeout
from tabulate import tabulate
import schedule
import time
from netmiko import ConnectHandler
import json
import sys


app = FastAPI()

with open('device_ip') as DEVICE_IP:
    for ip in DEVICE_IP:

        RTR = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': 'anwea',
            'password': '02anwe05',
            'secret': '02anwe05'}

        net_connect = ConnectHandler(**RTR)


#@app.get("/")
def intf_status():
    print("Checking ip address status for:", ip)

    try:
        net_connect.enable()
    except NetmikoTimeoutException:
        print('Device unreachable')

    except NetmikoAuthenticationException:
        print('Authentication Failed')

    except SSHException:
        print('Error reading SSH protocol banner')
        # continue

    except AuthenticationException:
        print('Failed Authentication Exception')

    except ReadTimeout:
        print('Netmiko ReadTimeout')
        # continue

    output = net_connect.send_command('sh int des', use_textfsm=True)
    #print(json.dumps(output, indent=2))
    print(tabulate(output, headers='keys', tablefmt='grid', stralign='center'))

"""
schedule.every(10).seconds.do(intf_status)

while True:
    schedule.run_pending()
    time.sleep(2)
"""

@app.get("/")
def tasks():
    intf_status()
#    schedule.every(10).seconds.do(intf_status)

#    while True:
#        schedule.run_pending()
#        time.sleep(1)


#tasks()

if __name__ == "__main__":
  uvicorn.run(app, port=8080, host="0.0.0.0")

