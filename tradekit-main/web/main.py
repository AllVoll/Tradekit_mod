from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncpg
from sqlalchemy.orm import Session
from . import schemas





app = FastAPI()

app.mount("/static", StaticFiles(directory="/app/web/static"), name="static")

templates = Jinja2Templates(directory="/app/web/templates")

@app.post("/api-keys/")
async def create_api_key(request: Request, 
                         name: str = Form(...), 
                         binance_key: str = Form(...), 
                         binance_secret: str = Form(...)):
    conn = None
    try:
        conn = await asyncpg.connect(user="tradekit", password="yourpassword", database="tradekit", host="localhost")
        query = "INSERT INTO api_keys (name, binance_key, binance_secret) VALUES ($1, $2, $3)"
        await conn.execute(query, name, binance_key, binance_secret)
        result = await conn.fetch("SELECT * FROM api_keys")
    finally:
        if conn:
            await conn.close()
    html_template = """
        <html>
            <head>
                <title>API Keys</title>
            </head>
            <body>
                <h1>API Keys</h1>
                <form method="post">
                    <label for="name">Name:</label>
                    <input type="text" name="name" required><br>
                    <label for="binance_key">Binance API Key:</label>
                    <input type="text" name="binance_key" required><br>
                    <label for="binance_secret">Binance API Secret:</label>
                    <input type="text" name="binance_secret" required><br>
                    <input type="submit" value="Create">
                </form>
                <h2>Existing Keys:</h2>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Binance API Key</th>
                        <th>Binance API Secret</th>
                    </tr>
                    %s
                </table>
            </body>
        </html>
    """ % "\n".join(f"<tr><td>{row['id']}</td><td>{row['name']}</td><td>{row['binance_key']}</td><td>{row['binance_secret']}</td></tr>" for row in result)
    return {"status": "success", "html_template": html_template}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tradingview_widget")
async def tradingview_widget(request: Request):
    return templates.TemplateResponse("tradingview_widget.html", {"request": request})

@app.get("/settings")
async def tradingview_widget(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/api_manager")
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


