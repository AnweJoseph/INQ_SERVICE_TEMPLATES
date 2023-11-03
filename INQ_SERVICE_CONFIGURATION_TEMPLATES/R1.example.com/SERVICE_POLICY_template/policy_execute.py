from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result
import time

from processing import processing_policy
processing_policy()

nr = InitNornir(config_file="config.yaml")

def execute_policy():
    print("########...PROCESSING SERVICE POLICY CONFIGURATION...########\n")
    time.sleep(2)

    print("Sending Configuration >>>\n")
    time.sleep(2)

    print("Loading Configuration...Please wait...")
    time.sleep(2)

    results = nr.run(task=netmiko_send_config, config_file='processed_policy')
    print_result(results)
    time.sleep(2)
    print("\Saving...")
    #results = nr.run(task=netmiko_save_config, cmd='write')
    time.sleep(3)        
    print("Done.")

def save_config():
    results = nr.run(task=netmiko_save_config, cmd='write')
    
execute_policy()
save_config()
