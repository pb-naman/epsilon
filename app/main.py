from typing import Any, Dict, AnyStr, List, Union
from fastapi import Request, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/runinstalledquery/")
async def run_installed_query(request: Request):
    return await request.json()


