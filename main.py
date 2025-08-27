from fastapi import FastAPI

from city.routes import city

app = FastAPI()
app.include_router(city)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
