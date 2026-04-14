from pydantic import BaseModel



class TopicRequest(BaseModel):
    user_query: str
