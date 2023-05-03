from fastapi import FastAPI
import uvicorn

from .auth.router import router as auth_router

app = FastAPI(
    title="FastApi-React-Mongo"
)

app.include_router(auth_router)

@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")