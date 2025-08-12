from fastapi import APIRouter
from app.model import debug_code, get_context

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to Pippy-Debugger! I'm here to help you debug your code."}

@router.post("/debug")   
async def debug(code: str, context: bool):
    
    if context:
        try:
            answer = get_context(code)
            return {"answer": answer}
        except Exception as e:
            print("ERROR:", e)
            return {"error": str(e)}
        
    else:
        try:
            answer = debug_code(code)
            return {"answer": answer}
        except Exception as e:
            print("ERROR:", e)
            return {"error": str(e)}
