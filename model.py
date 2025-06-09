from transformers import pipeline

model = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct", device=-1)

def debug_code(code: str):
    prompt = f"Here is some Python code:\n{code}\n\nWhat are the potential bugs or improvements? Give debugging tips:"
    result = model(prompt, max_new_tokens=256, truncation=True, do_sample=True)
    return result[0]["generated_text"]
