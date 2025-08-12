import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from app.prompts.prompts import CODE_DEBUG_PROMPT, CODE_CONTEXT_PROMPT

load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

model = init_chat_model("gemma-3-12b-it", model_provider="google_genai")

def debug_code(code: str):
    prompt = ChatPromptTemplate.from_template(CODE_DEBUG_PROMPT)
    
    chain = prompt|model
    output = chain.invoke({"code": code})
    
    response = output.content
    
    return response


def get_context(code: str):
    prompt = ChatPromptTemplate.from_template(CODE_CONTEXT_PROMPT)
    
    chain = prompt|model
    output = chain.invoke({"code": code})

    response = output.content
    
    return response
