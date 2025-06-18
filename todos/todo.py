from fastapi import APIRouter, Path, Query, HTTPException, status
from models.todo import Todo, TodoItem, TodoItems
from typing import List, Dict

todo_router = APIRouter()

todo_list: List[Todo]

'''
status_code를 추가함으로써 기본 응답코드를 200에서 201로 변경한다. 
''' 
@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully"
    }

'''
response_model을 지정함으로써 응답에서 제공하는 필드가 달라진다.
여기서는 id가 제외된다.
'''
# @todo_router.get("/todo")
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }

# path 알아보기
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(query: str = Query(None), todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:

    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
        
    # return {
    #     "message": "Todo with supplied ID doesn't exist"
    # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., titld="The ID of the todo to retrieve.")) -> dict:

    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully"
            }
    # return {
    #     "message": "Todo with supplied ID doesn't exist"
    # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:

    for index in range(len(todo_list)):
        todo = todo_list[index]

        if todo.id  == todo_id:
            todo_list.pop(index)
            
            return {
                "message": "Todo deleted successfully"
            }
        
    # return {
    #     "message": "Todo with supplied ID doesn't exist"
    # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully"
    }