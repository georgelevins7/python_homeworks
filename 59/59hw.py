
from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.1-flash-lite"
MAX_ATTEMPTS = 3

########### State ############

class State(TypedDict):
    ingredients: str
    recipe: str
    feedback: str
    approved: bool
    attempts: int


########### Nodes ############

def generate_recipe(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = f"""
    Generate a recipe based on the following ingredients: {state['ingredients']}

    Include ingredient quantities, cooking steps and cooking time.
    """

    response = llm.invoke(prompt)

    return {"recipe": response.text}


def check_recipe(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = f"""
    Check the following recipe based on these criteria:

    - Are all the provided ingredients used?
    - Is the recipe clear and easy to understand?
    - Does the recipe include step-by-step cooking instructions?
    - Are the ingredient quantities logical and realistic?

    Ingredients: {state['ingredients']}
    Recipe: {state['recipe']}

    If the recipe meets all criteria, approve it.
    Otherwise, explain what needs to be improved.

    Return your answer strictly in this format:
    Approved: True or False
    Feedback: Your explanation

    Do not include any other text.
    """

    response = llm.invoke(prompt)

    approved = "Approved: True" in response.text

    return {
        "feedback": response.text,
        "approved": approved,
        "attempts": state["attempts"] + 1
    }


def improve_recipe(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = f"""
    Improve the following recipe based on the feedback provided:

    Ingredients: {state['ingredients']}
    Recipe: {state['recipe']}
    Feedback: {state['feedback']}

    Fix the problems mentioned in the feedback.

    Return only the improved recipe.
    """

    response = llm.invoke(prompt)

    return {"recipe": response.text}


########### Conditions ############

def approve_continue(state: State):

    if state["approved"]:
        return END

    if state["attempts"] >= MAX_ATTEMPTS:
        return END

    return "improve_recipe"


########### Graph ############

graph_builder = StateGraph(State)

graph_builder.add_node("generate_recipe", generate_recipe)
graph_builder.add_node("check_recipe", check_recipe)
graph_builder.add_node("improve_recipe", improve_recipe)

graph_builder.add_edge(START, "generate_recipe")
graph_builder.add_edge("generate_recipe", "check_recipe")

graph_builder.add_conditional_edges("check_recipe", approve_continue)

graph_builder.add_edge("improve_recipe", "check_recipe")

graph = graph_builder.compile()


########### Run ############

initial_state = {
    "ingredients": "chicken, rice, onion, tomato",
    "recipe": "",
    "feedback": "",
    "approved": False,
    "attempts": 0
}

result = graph.invoke(initial_state)

print("\n=== FINAL RECIPE ===")
print(result["recipe"])

print("\n=== FEEDBACK ===")
print(result["feedback"])

print("\nApproved:", result["approved"])
print("Attempts:", result["attempts"])