from mcp_client import list_mcp_tools, call_mcp_tool
from llm_ollama import call_llm
from prompt import build_prompt
from prompt import build_topic_prompt
from tutor_model import TutorResponse, TutorRequest
from tutor_topic_model import TopicRequest
from langchain_core.messages import AIMessage
import json


class ChatAgent:

    def needs_tool_execution(self, llm_response: AIMessage) -> bool:
        return bool(getattr(llm_response, "tool_calls", []))

    async def run(self, request ) -> str:

        # Step 1: fetch tools from MCP server
        tools_response = await list_mcp_tools()

        tools = [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema,
                },
            }
            for tool in tools_response.tools
        ]

        # Step1: build Topic Prompt
        if isinstance(request, TutorRequest):
           custom_prompt = build_prompt(
               subject=request.subject,
               level=request.level,
               goal=request.goal
           )
        else:
           custom_prompt = build_topic_prompt(
               user_query=request.user_query
            )

        # Step 3: first LLM call
        llm_response = call_llm(
            system_prompt=custom_prompt,
            user_query=request.user_query,
            tools=tools
        )

        # Step 4: execute MCP tool if requested
        if self.needs_tool_execution(llm_response):

            tool_call = llm_response.tool_calls[0]

            tool_result = await call_mcp_tool(
                tool_name=tool_call["name"],
                arguments=tool_call["args"]
            )

            # Step 5: second LLM call with tool result
            final_prompt = f"""
            {custom_prompt}

            Tool Result:
            {tool_result}

            Now answer the student's question.
            """

            final_response = call_llm(
                system_prompt=final_prompt,
                user_query=request.user_query,
                tools=tools
            )


            return final_response.content
        
        if isinstance(request, TopicRequest):
          return safe_json_parse(llm_response.content)

        return {"response": llm_response.content}
    


def safe_json_parse(content: str):
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "response": content,
            "error": "Invalid or incomplete JSON from model"
        }