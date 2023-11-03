from pydantic import BaseModel

class Todo(BaseModel):
    client_vrf: str
    rd: str
    rt_export: str
    rt_import: str
