import os
from fastapi import FastAPI, HTTPException
from agent import ChatAgent
from tutor_model import TutorRequest, TutorResponse
from  tutor_topic_model import TopicRequest

app = FastAPI()

chat_agent = ChatAgent()


@app.post("/ask", response_model=TutorResponse)
async def ask_tutor(request: TutorRequest):

    if not request.user_query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )

    result = await chat_agent.run(request)

    return TutorResponse(response=result)

@app.post("/topics")
async def get_topics(request: TopicRequest):
    if not request.user_query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )

    result = await chat_agent.run(request)
    return {"response": result}

@app.get("/")
def health():
    return {"status": "running"}