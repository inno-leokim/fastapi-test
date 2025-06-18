from pydantic import BaseModel

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
