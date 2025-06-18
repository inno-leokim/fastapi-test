from fastapi import FastAPI
import uvicorn
from todos.todo import todo_router
from hello import hello_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

app.include_router(todo_router, prefix="/api")
app.include_router(hello_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("api:app", host='0.0.0.0', port=8000, reload=True)
