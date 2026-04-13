from typing import Any, Optional
import os


PROMPT_PATH = "master_prompt.txt"


def get_prompt(query: str, pdf_path: str = None, tool_result: Optional[Any] = None) -> str:
    prompt = f"""You are a helpful AI assistant. Your task is to answer the user's query using the information provided.

    ## User Query: {query}

    ## PDF Path: {pdf_path if pdf_path else "No pdf path provided"}

    ## Tool Result: {tool_result if tool_result else "No tool result available"}

    ## Instructions:

    1. If tool result is available:
    - You MUST use the information from the tool result to answer the user's query
    - Base your answer primarily on the tool result content
    - Do NOT ignore the tool result or answer from general knowledge when tool result exists

    2. If tool result is not available:
    - Answer based on your general knowledge
    - Be clear that you're answering without specific document context
   
    """
    return prompt


def load_prompt_template():
    with open(PROMPT_PATH, "r") as file:
        return file.read()


def build_prompt(subject, level, goal):
    template = load_prompt_template()

    return template.format(
        subject=subject,
        level=level,
        goal=goal
    )
