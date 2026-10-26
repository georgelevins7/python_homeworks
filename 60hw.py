from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

MODEL = "gemini-3.1-flash-lite"

########### State ############

class State(TypedDict):
    user_request: str
    destination_info: str
    food_info: str
    budget_info: str
    final_plan: str


########### Nodes ############

def destination_agent(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = [
        SystemMessage(content=
        f"""
        You are a travel destination expert.
        Your task is to analyze the user's request {state['user_request']} and provide recommendations 
        for the destination and activities that might interest the user at the specified location.
        """
        ),
        HumanMessage(content=f"User request: {state['user_request']}")
    ]
    response = llm.invoke(prompt)

    return {"destination_info": response.text}


def food_agent(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = [
        SystemMessage(content=
        f"""
        You are a food expert.
        Your task is to analyze the user's request {state['user_request']} and provide recommendations 
        for food options that might interest the user at the specified destination.
        Consider the user's budget and preferences when making recommendations.
        """
        ),
        HumanMessage(content=f"User request: {state['user_request']}")
    ]

    response = llm.invoke(prompt)

    return {"food_info": response.text}


def budget_agent(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = [
        SystemMessage(content=
        f"""
        You are a travel budget expert. 
        Estimate realistic travel costs based on the user's budget and preferences.
        Provide estimated costs for:
        - Hotel
        - Food
        - Transportation
        - Activities

        Include the estimated total budget.
        """
        ),
        HumanMessage(content=f"User request: {state['user_request']}")
    ]

    response = llm.invoke(prompt)

    return {"budget_info": response.text}

def planner_agent(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = [
        SystemMessage(content=
        f"""
        You are a travel planner expert.
        Your task is to create a final travel plan based on the user's request {state['user_request']}, 
        destination information, food information , 
        and budget information. Use only the information provided by the other agents.
        Do not invent additional recommendations or costs.
        """
        ),
        HumanMessage(content=f"""User request: {state['user_request']},
                    Destination info: {state['destination_info']},
                    Food info: {state['food_info']},
                    Budget info: {state['budget_info']}
                     """)
    ]

    response = llm.invoke(prompt)

    return {"final_plan": response.text}


########### Graph ############

builder = StateGraph(State)


builder.add_node("destination_agent", destination_agent)
builder.add_node("food_agent", food_agent)
builder.add_node("budget_agent", budget_agent)
builder.add_node("planner_agent", planner_agent)

builder.add_edge(START, "destination_agent")
builder.add_edge(START, "food_agent")
builder.add_edge(START, "budget_agent")
builder.add_edge(["destination_agent", "food_agent", "budget_agent"], "planner_agent")
builder.add_edge("planner_agent", END)

graph = builder.compile()


########### Run ############

initial_state = {
    "user_request": input("Enter your travel request: "),
    "destination_info": "",
    "food_info": "",
    "budget_info": "",
    "final_plan": ""
}

result = graph.invoke(initial_state)

print("\n=== FINAL PLAN ===")
print(result["final_plan"])