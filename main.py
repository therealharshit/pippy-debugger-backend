from fastapi import FastAPI
from pydantic import BaseModel
from model import debug_code, get_context

app = FastAPI()

class DebugQuery(BaseModel):
    code: str

class ContextQuery(BaseModel):
    code: str

@app.get("/")
def root():
    return {"message": "Welcome to Pippy-Debugger! I'm here to help you debug your code."}

@app.post("/debug")
async def debug_endpoint(debug_query: DebugQuery):
    tips = debug_code(debug_query.code)
    return {"debug_tips": tips}

@app.post("/context")
async def context_endpoint(context_query: ContextQuery):
    context = get_context(context_query.code)
    return {"code_context": context}
