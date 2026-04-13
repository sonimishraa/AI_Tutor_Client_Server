from typing import List,Dict,Any,Optional
from langchain_ollama import ChatOllama

MODEL_NAME= "qwen2.5-coder:14b"

llm = ChatOllama(model=MODEL_NAME,
                 base_url ="http://127.0.0.1:11434",
    temperature=0.3,
    num_predict=120) ## use correct port for model base url


def call_llm(system_prompt, user_query, tools=None):
    response = llm.invoke(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        tools=tools
    )
    return response