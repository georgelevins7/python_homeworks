from pydantic import BaseModel

class TravelRequest(BaseModel):
    request: str

class TravelResponse(BaseModel):
    final_plan: str