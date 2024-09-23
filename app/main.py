from typing import Any, Dict, AnyStr, List, Union
from fastapi import Request, FastAPI, HTTPException
from pydantic import BaseModel
from utils import tg_runInstalledQuery
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:80",
]

class Item(BaseModel):
    queryname: str
    params: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/runinstalledquery/")
def run_installed_query(item: Item):
    if item.queryname == "" or item.params == "":
        raise HTTPException(status_code=400, detail="query name or query parameters missing")
    try:
        params = json.loads(item.params)
    except:
        raise HTTPException(status_code=400, detail="invalid query parameters")
    query_output = tg_runInstalledQuery(item.queryname, params)
    return query_output