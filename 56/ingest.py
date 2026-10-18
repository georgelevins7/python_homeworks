from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from database import engine
from sqlalchemy.orm import Session
from models import Document

load_dotenv()

EMBEDDING_MODEL = "gemini-embedding-001"

client = genai.Client()

loader = UnstructuredMarkdownLoader("56/data/hotel_info.md")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=30)
chunks = splitter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

embeddings = [item.values for item in result.embeddings]

with Session(engine) as session:
    for chunk, embedding in zip(chunks, embeddings):
        doc = Document(
            content=chunk.page_content,
            embedding=embedding,
            chunk_metadata=chunk.metadata
        )
        session.add(doc)
    session.commit()