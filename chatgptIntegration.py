import openai
import os
import pandas as pd
import time

openai.api_key = os.getenv("OPENAI_API_KEY")


#def get_completion(prompt, model="gpt-3.5-turbo"):
def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,)
    return response.choices[0].message["content"]
