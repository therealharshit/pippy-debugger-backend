from transformers import pipeline

model = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct", device=-1)

def debug_code(code: str):
    prompt = f"""
    You are an expert Python developer. Analyze the following Python code and provide helpful debugging suggestions in less than 250 words.
    
    Code:
    ```
    {code}
    ```

    Instructions:
    1. Identify any syntax errors, logical mistakes, or bad practices.
    2. Explain *why* each issue might cause problems.
    3. Suggest clear and simple ways to fix or improve the code.
    4. If the code looks fine, mention that too.

    Be concise and beginner-friendly.

    ### Response:
    """

    output = model(prompt, max_new_tokens=512, do_sample=True)
    # The result is a list of dicts: [{'generated_text': '...'}]
    response = output[0]['generated_text']

    # Clean the response to remove the original prompt
    if "### Response:" in response:
        response = response.split("### Response:")[-1].strip()

    return response
