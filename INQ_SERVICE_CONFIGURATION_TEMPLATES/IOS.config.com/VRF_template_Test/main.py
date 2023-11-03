from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import pymongo


class VRF(BaseModel):
    client_vrf: str
    rd: str
    rt_export: str
    rt_import: str


app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["VRFDataBase"]
collection = db["VRFdata"]


@app.post("/VRF_Data/")
async def create_vrf(vrf: VRF):
    return vrf
    collection.insert_one(vrf)
