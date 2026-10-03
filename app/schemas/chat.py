from typing import Optional
from pydantic import BaseModel
class AskRequest(BaseModel):
    question:str
    provider:str
    model:Optional[str] = None

class AskResponse(BaseModel):
    answer:str
    provider:str
    model:str|None = None
    






