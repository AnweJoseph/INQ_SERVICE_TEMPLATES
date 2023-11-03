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
from enum import Enum
from typing import Optional

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

vrf = {
        '101:101': {
              "client_vrf": "SAT3INTERNET",
              "rd": "101:101",
              "rt_export": "101:101",
              "rt_import": "101:101"

            }
    }

class Modelname(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
def intf_status():
    return {"Progress": "Checking interface status for this device"}

@app.get("/query-rd")
def query_rd(*, rd: Optional[str] = None, rt_import: str):
    for i in vrf:
        if vrf[i]['rd'] == rd:
           return vrf[i]
    return {"VRF": "This is not a client vrf"}

@app.get("/get-model-name/{modelname}")
def get_model(modelname: Modelname):
    if modelname is Modelname.alexnet:
        return {"modelname": modelname, "message": "Deep Learning FTW!"}
    if modelname.value == "lenet":
        return {"modelname": modelname, "message": "LeCNN all the messages"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/get-vrf/{vrf_id}")
def get_vrf(vrf_id: str):
    return vrf[vrf_id]

if __name__ == "__main1__":
  uvicorn.run(app, port=8080, host="0.0.0.0")


