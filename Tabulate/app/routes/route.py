from fastapi import APIRouter
from models.todos import Todo
from config.database import collection
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_todos():
    todos = list_serial(collection.find())
    return todos

    
@router.post("/")
async def post_todo(todo: Todo):
    collection.insert_one(dict(todo))
