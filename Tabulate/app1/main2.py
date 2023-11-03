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
import pymongo

import contextlib
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi.encoders import jsonable_encoder


#app = FastAPI()

from processed import intf_status
intf_status()
time.sleep(5)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DeviceInterfaceStats"]
collection = db["status"]


with open('processed.json', 'r') as f:
    status = json.load(f)


for intf_stat in status:
    collection.insert_one(intf_stat)

client.close()

app = FastAPI()
#client = MongoClient('mongodb://localhost:27017/')

@app.get("/")
def intf_status():
    return {"Progress": "Checking interface status for this device"}
    #return (status)


if __name__ == "__main1__":
  uvicorn.run(app, port=8080, host="0.0.0.0")


