from pydantic import BaseModel


class TutorRequest(BaseModel):
    subject: str
    level: str
    goal: str | None = "AI Learning"
    user_query: str


class TutorResponse(BaseModel):
    response: str