import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from app.prompts.prompts import CODE_DEBUG_PROMPT, CODE_CONTEXT_PROMPT, KIDS_DEBUG_PROMPT, KIDS_CONTEXT_PROMPT

load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

model = init_chat_model("gemma-3-27b-it", model_provider="google_genai")
output_parser = StrOutputParser()

def debug_code(code: str):
    debug_prompt = ChatPromptTemplate.from_template(CODE_DEBUG_PROMPT)
    kids_prompt = ChatPromptTemplate.from_template(KIDS_DEBUG_PROMPT)
    
    chain = debug_prompt|model|output_parser|kids_prompt|model|output_parser
    output = chain.invoke({"code": code})
    
    response = output
    
    return response


def get_context(code: str):
    context_prompt = ChatPromptTemplate.from_template(CODE_CONTEXT_PROMPT)
    kids_prompt = ChatPromptTemplate.from_template(KIDS_CONTEXT_PROMPT)
    
    chain = context_prompt|model|output_parser|kids_prompt|model|output_parser
    output = chain.invoke({"code": code})

    response = output
    
    return response
