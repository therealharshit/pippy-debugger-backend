from transformers import pipeline

model = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct", device=-1)

def debug_code(code: str):
    prompt = f"""
    You are an expert Python developer. Analyze the following Python code and provide helpful debugging suggestions.
    
    Code:
    ```
    {code}
    ```

    Instructions:
    1. Identify any syntax errors, logical mistakes, or bad practices.
    2. Explain *why* each issue might cause problems.
    3. Suggest clear and simple ways to fix or improve the code.
    4. If the code looks fine, mention that too.
    5. Do not give full corrected code, instead give psuedo code or code snippets.
    6. Generate response in LESS THAN 300 WORDS.

    Be concise and beginner-friendly.

    ### Response:

    ### Sugar-AI:
    """

    output = model(prompt, max_new_tokens=512, do_sample=True)

    response = output[0]['generated_text']

    # Clean the response to remove the original prompt
    if "### Response:" in response:
        response = response.split("### Response:")[-1].strip()

    return response


def get_context(code: str):

    prompt = f"""
    You are an expert Python developer.Without correcting or analyzing errors, just tell me the context or intent - what the code is trying to do.
    
    Code:
    ```
    {code}
    ```

    Instructions:
    1. Only explain the intention.
    2. Do not correct syntax or mention errors.
    3. Do not suggest improvements or alternatives.
    4. Be concise and focus only on the context or goal the code seems to represent.
    5. Keep the response as Short as Possible.
    6. Generate response in LESS THAN 100 WORDS.

    Be concise and beginner-friendly.

    ### Response:

    ### Sugar-AI:
    """

    output = model(prompt, max_new_tokens=512, do_sample=True)

    response = output[0]['generated_text']

    # Clean the response to remove the original prompt
    if "### Response:" in response:
        response = response.split("### Response:")[-1].strip()

    return response