from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal

load_dotenv()

GEMINI_MODEL = "gemini-3.1-flash-lite"

review_1 = "This laptop is fast, lightweight, and has an excellent display. " \
"However, its battery life could be better."
review_2 = "The phone is slow, overheats frequently, and the camera quality is disappointing."
review_3 = "The headphones have average sound quality. " \
"They are comfortable, but the price is relatively high."

# reviews = [review_1, review_2, review_3]

model = ChatGoogleGenerativeAI(model=GEMINI_MODEL)


class ProductReview(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    pros: list[str]
    cons: list[str]
    summary: str
    recommend: bool

parser = PydanticOutputParser(pydantic_object=ProductReview)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert product reviewer. "
    "Extract structured information from the product review."
    "Base your analysis only on the provided review. "
    "Do not invent product features or problems. {format_instructions}"),
    ("human", "{review}")
])

chain = prompt | model | parser

# for review in reviews:
#     response = chain.invoke(
#         {
#             "review": review,
#             "format_instructions": parser.get_format_instructions()
#         }
#     )

#     print(f"\n-- Review {reviews.index(review) + 1} --")
#     print(response.model_dump_json(indent=2))
#     print(type(response))
response = chain.invoke(
    {
        "review": review_2,
        "format_instructions": parser.get_format_instructions()
        }
        )

print(response)
print(type(response))
