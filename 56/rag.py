from dotenv import load_dotenv
load_dotenv()

from google import genai
from sqlalchemy.orm import Session
from sqlalchemy import select
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from database import engine
from models import Document

client = genai.Client()

EMBEDDING_MODEL = "gemini-embedding-001"

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

prompt = ChatPromptTemplate.from_messages(
    [
    ("system", 
    """
    You are a helpful assistant. Answer the question based on the provided context. "
    Don't add any information that is not present in the context. "
    If the answer is not contained within the context, respond with \"I don't know.\".
    """
    ),
    ("human", "Context:\n{context}\nQuestion:\n{question}")

    ]
)


def retrieve_documents(question: str):
    query_result = (client.models.embed_content(
        model="gemini-embedding-001",
        contents=[question]
    ))

    query_embedding = query_result.embeddings[0].values

    query = select(Document).order_by(Document.embedding.cosine_distance(query_embedding)).limit(3)

    with Session(engine) as session:
        results = session.execute(query).scalars().all()

    return results

def format_documents(documents):
    return "\n\n".join(doc.content for doc in documents)

def answer_question(question: str):
    documents = retrieve_documents(question)
    context = format_documents(documents)
    chain = prompt | llm | StrOutputParser()

    return chain.invoke(
        {
        "question": question,
        "context": context
        }
    )


while True:
    question = input("Please enter your question: ")
    if question == "exit":
        break

    response = answer_question(question)
    print(response)


######################## Questions to copy #########################################

#რამდენი ღირს ოთხი ადამიანისთვის განკუთვნილი ნომერი?
#საუზმე შედის ნომრის ფასში?
#შემიძლია თუ არა ჯავშნის გაუქმება ჩამოსვლამდე ერთი დღით ადრე?
#რომელ საათზე უნდა დავტოვო ნომერი?
#რა აქტივობებია ხელმისაწვდომი სტუმრებისთვის?
#რა პირობებია შინაური ცხოველის წამოყვანისთვის?
#რა მოხდება, თუ ჯავშნის გარეშე კი არა, დაჯავშნილი ნომრით საერთოდ არ მივალ?