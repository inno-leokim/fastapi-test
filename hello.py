from fastapi import APIRouter

hello_router=APIRouter()

@hello_router.get("/hello")
async def say_hello() -> dict:
    return {
        "message": "Hello World"
    }