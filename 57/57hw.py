from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import ToolMessage

load_dotenv()

MODEL = "gemini-3.1-flash-lite"

@tool
def search_hotel(city: str):
    """Search for hotels in the specified city."""

    hotels = {
        "Tbilisi": {
            "Griffin Hotel": 120, 
            "Sunset Inn": 180, 
            "Grand Plaza": 250
            },
        "Batumi": {
            "Oceanview Hotel": 180, 
            "Palm Beach Hotel": 130, 
            "Grand View Hotel": 210
        }
    }
    if city not in hotels:
        return f"No hotels found in {city}."
    return f"Searching for hotels in {city}: {', '.join([f'{name} ({price} GEL)' for name, price in hotels.get(city, {}).items()])}"

@tool
def get_exchange_rate(currency: str):
    """Get the exchange rate for the specified currency."""

    exchange_rates = {
        "usd": 2.7,
        "eur": 3.15,
        "gbp": 3.6
    }
    rate = exchange_rates.get(currency.lower())
    if not rate:
        return f"Exchange rate for {currency.upper()} not found."
    return f"1 {currency.upper()} = {rate} GEL"

@tool
def search_attractions(city: str):
    """Search for attractions in the specified city."""

    attractions = {
        "Tbilisi": ["Narikala Fortress", "Old Tbilisi", "Mtatsminda Park"],
        "Batumi": ["Batumi Boulevard", "Ali and Nino Statue", "Batumi Botanical Garden"]
    }
    if city not in attractions:
        return f"No attractions found in {city}."
    return f"Searching for attractions in {city}: {', '.join(attractions.get(city, []))}"

llm = ChatGoogleGenerativeAI(model=MODEL)

tools = [search_hotel, get_exchange_rate, search_attractions]

llm_with_tools = llm.bind_tools(tools)

question = input("Please enter your question: ")
response = llm_with_tools.invoke(question)

tool_results = []

for tool_call in response.tool_calls:
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    print(f"Tool called: {tool_name} with arguments: {tool_args}")

    selected_tool = next((tool for tool in tools if tool_name == tool.name))

    result = selected_tool.invoke(tool_args)
    tool_results.append(
        ToolMessage(
            tool_call_id=tool_call["id"],
            content=str(result)
        )
    )

message = [
    {
        "role": "user",
        "content": question
    },
    response,
    *tool_results
]

final_response = llm_with_tools.invoke(message)
print(f"Final response: {final_response.text}")