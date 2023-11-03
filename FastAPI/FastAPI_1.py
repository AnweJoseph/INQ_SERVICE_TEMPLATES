from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()


class VRF(str, Enum):
    client_vrf = "GT_BANK"
    rd = "100:100"
    rt_import = "100:100"
    rt_export = "100:100"
    text = "200:200"


@app.get("/{vrf}")
async def create_get(*, vrf: int | None = None):
    return {"VRF": vrf}


@app.get("/items/{vrf}")
async def item_value(vrf: VRF):
    if VRF.client_vrf is vrf:
        return {"VRF": "The is GT_BANK detail"}

    if vrf.value != "100:100":
        return {"Message": "This rt_export is not correct"}
