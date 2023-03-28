from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.api.api_manager import router as api_key_router


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tradingview_widget")
async def tradingview_widget(request: Request):
    return templates.TemplateResponse("tradingview_widget.html", {"request": request})

@app.get("/settings")
async def tradingview_widget(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/settings/api_manager")
async def api_manager(request: Request):
    return templates.TemplateResponse("api_manager.html", {"request": request})

@app.get("/settings/coinlist_manager")
async def coinlist_manager(request: Request):
    return templates.TemplateResponse("coinlist_manager.html", {"request": request})

@app.get("/settings/depo_manager")
async def depo_manager(request: Request):
    return templates.TemplateResponse("depo_manager.html", {"request": request})

@app.get("/settings/strategy_manager")
async def strategy_manager(request: Request):
    return templates.TemplateResponse("strategy_manager.html", {"request": request})    