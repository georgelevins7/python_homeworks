from schemas import TravelRequest, TravelResponse
from fastapi import FastAPI
from agents import graph

app = FastAPI(
    title="Travel Planner API",
    description="API for planning travel itineraries",
    version="1.0.0"
)

@app.post("/travel", response_model=TravelResponse)
def plan_travel(request: TravelRequest):
    initial_state = {
    "user_request": request.request,
    "destination_info": "",
    "food_info": "",
    "budget_info": "",
    "final_plan": ""
}
    result = graph.invoke(initial_state)
    return TravelResponse(final_plan=result["final_plan"])