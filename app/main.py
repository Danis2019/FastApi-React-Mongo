from fastapi import FastAPI, Request
import uvicorn

from .auth.router import router as auth_router

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

react_templates = Jinja2Templates(directory="app/frontend/react_main_page/build/")

app = FastAPI(
    title="FastApi-React-Mongo"
)

app.mount('/static', StaticFiles(directory="app/frontend/react_main_page/build/static"), 'static')

app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {'request': request}
    return react_templates.TemplateResponse("index.html", context)

@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")