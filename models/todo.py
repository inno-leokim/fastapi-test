from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int 
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "item": "Example Schema!",
                    "status": "Added"
                }
            }
        }

class TodoItem(BaseModel):
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "item": {
                    "item": "Example Schema!",
                    "status": "Edited"
                }
            }    
        }

# id를 제외
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": {
                            "item": "Editted Schema 1!",
                            "stataus": "Edited"
                        }
                    },
                    {
                        "item": {
                            "item": "Editted Schema 2!",
                            "stataus": "Edited"
                        }
                    }
                ]
            }
        }