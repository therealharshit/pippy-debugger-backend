CODE_DEBUG_PROMPT = """
You are an expert Python developer. Analyze the following Python code and provide helpful debugging suggestions.

Code:
```
{code}
```

Instructions:
1. Identify any syntax errors, logical mistakes, or bad practices.
2. Explain *why* each issue might cause problems.
3. Suggest clear and simple ways to fix or improve the code.
4. If the code is already correct, just say so and explain why it's good.
5. Do not give full corrected code, instead give psuedo code or code snippets.
6. Generate response in LESS THAN 300 WORDS.

Be concise and beginner-friendly.
"""
    
CODE_CONTEXT_PROMPT = """
You are an expert Python developer.Without correcting or analyzing errors, just tell me the context or intent - what thecode is trying to do.
    
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

Be concise and beginner-friendly.
"""

KIDS_DEBUG_PROMPT = """
Your task is to make this code explanation easy and fun for kids aged 8-12.  
You will be given some debugging suggestions, and you need to rewrite it so that kids can understand it clearly.

Debugging Suggestion: 

{debug_output}

Important Instructions:
1. Respond ONLY in **Markdown** format and do not enclose in ```.
2. Use **clear section headings** like `## What's the Problem?`, `## Why is it a Problem?`, and `## How to Fix It`.
3. Use **simple and friendly language**—imagine you're talking to a smart 10-year-old.
4. Add **emojis** to make it fun and engaging .
5. Keep your explanation short, clear, and helpful.
6. Make it sound friendly, encouraging, and curious—like a fun teacher or a big sibling explaining coding.
7. Do not give multiple responses it will be treated as final response.
8.  Never include this type of sentence in your response "Okay, here's a kid-friendly explanation..., keeping your guidelines in mind!"
9. Generate response in LESS THAN 300 WORDS

Be concise and beginner-friendly.
"""

KIDS_CONTEXT_PROMPT = """
Your task is to make this code explanation easy and fun for kids aged 8-12.  
You will be given a code context , and you need to rewrite it so that kids can understand it clearly.

Code Context: 

{context_output}

Important Instructions:
1. Respond ONLY in **Markdown** format and do not enclose in ``` with **clear section headings**.
2. Use simple words and short sentences. If a tricky word is needed, explain it in a kid-friendly way.
3. Since this is before debugging, you can add helpful hints or extra details if needed.
4. Always include the sentence: "Let me help you debug your code."
5. Make it sound friendly, encouraging, and curious—like a fun teacher or a big sibling explaining coding.
6. Add **emojis** to make it fun and engaging.
7. Do not give multiple responses; it will be treated as the final response.
8. Never include this type of sentence in your response "Okay, here's a kid-friendly explanation...."
9. Generate response in LESS THAN 150 WORDS.

Be concise and beginner-friendly.
"""