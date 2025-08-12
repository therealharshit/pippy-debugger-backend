from transformers import pipeline
from app.prompts.prompts import CODE_DEBUG_PROMPT, CODE_CONTEXT_PROMPT

model = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct", device=-1)

def debug_code(code: str):
    prompt = CODE_DEBUG_PROMPT.format(code=code)
    output = model(prompt, max_new_tokens=512, do_sample=True)

    response = output[0]['generated_text']

    if "### Response:" in response:
        response = response.split("### Response:")[-1].strip()

    return response


def get_context(code: str):
    prompt = CODE_CONTEXT_PROMPT.format(code=code)
    output = model(prompt, max_new_tokens=512, do_sample=True)

    response = output[0]['generated_text']

    if "### Response:" in response:
        response = response.split("### Response:")[-1].strip()

    return response
