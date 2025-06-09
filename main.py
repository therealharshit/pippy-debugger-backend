from fastapi import FastAPI
from pydantic import BaseModel
from model import debug_code

app = FastAPI()

class DebugQuery(BaseModel):
    code: str

@app.get("/")
def root():
    return {"message": "Welcome to Pippy-Debugger! I'm here to help you debug your code."}

@app.post("/debug")
async def debug_endpoint(debug_query: DebugQuery):
    tips = debug_code(debug_query.code)
    return {"debug_tips": tips}
