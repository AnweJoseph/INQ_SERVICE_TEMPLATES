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


with open('device_ip') as DEVICE_IP:
    for ip in DEVICE_IP:

        RTR = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': 'anwea',
            'password': '02anwe05',
            'secret': '02anwe05'}

        net_connect = ConnectHandler(**RTR)


def intf_status():
    
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
        
    output = net_connect.send_command('sh int des', use_textfsm=True)
    output = (json.dumps(output, indent=2))

    save_template = open('processed.json', 'w')
    save_template.write(output)
    save_template.close


intf_status()

