from pymongo import MongoClient
from pydantic import BaseModel
from schema.schemas import list_serial
from bson import ObjectId
from fastapi import FastAPI
import json


app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["vrf_db"]
collection = db["vrfData"]


class Vrf(BaseModel):
    cct_id: str
    client_vrf: str
    rd: str
    rt_export: str
    rt_import: str


@app.get("/")
def get_vrf():
    todos = list_serial(collection.find())
    return todos


@app.get("/{cct}")
def get_vrf(cct: str):
    todos = list_serial(collection.find({"_id": ObjectId(cct)}))
    return todos


@app.post("/")
def post_vrf(todo: Vrf):
    collection.insert_one(dict(todo))
