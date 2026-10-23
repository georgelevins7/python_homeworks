from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

MODEL = "gemini-3.1-flash-lite"

########### State ############

class State(TypedDict):
    product_text: str
    product_info: str
    marketing_text: str
    final_description: str

########### Nodes ############

def extract(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = f"""Extract product information from the following text:\n{state['product_text']}
    Use the following format for the extracted information:
        Product: <extracted product name>
        Display: <extracted display information>
        Storage: <extracted storage information>
        Processor: <extracted processor information>
        Camera: <extracted camera information>
        Connector: <extracted connector information>
        Colors: <extracted colors information>
    """

    response = llm.invoke(prompt)
    return {"product_info": response.text}

def marketing(state: State):

    llm = ChatGoogleGenerativeAI(model=MODEL)

    prompt = f"""
    Create a marketing text for the following product information:\n{state['product_info']}
    """

    response = llm.invoke(prompt)
    return {"marketing_text": response.text}

def format(state: State):

    return {"final_description": f"=== PRODUCT DESCRIPTION ===\n{state['marketing_text']}\n=== END ==="}

########### Graph ############

graph = StateGraph(State)
graph.add_node("extract", extract)
graph.add_node("marketing", marketing)
graph.add_node("format", format)

graph.add_edge(START, "extract")
graph.add_edge("extract", "marketing")
graph.add_edge("marketing", "format")
graph.add_edge("format", END)

graph = graph.compile()

while True:
    product_text = input("Enter product text: ")
    if product_text == "exit":
        break
    result = graph.invoke({
        "product_text": product_text,
        "product_info": "",
        "marketing_text": "",
        "final_description": ""
    })
    print(result["final_description"])