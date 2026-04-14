from pydantic import BaseModel
from typing import List


class TopicItem(BaseModel):
    id: int
    title: str
    description: str
    level: str


class TopicResponse(BaseModel):
    subject: str
    topics: List[TopicItem]