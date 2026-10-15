from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

EMBEDDING_MODEL = "gemini-embedding-001"

client = genai.Client()

load = UnstructuredMarkdownLoader("55/hotel_info.md")

docs = load.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=30)
chunks = splitter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

embedding = [item.values for item in result.embeddings]

question = input("Enter your question: ")

query_embedding = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=question
)

query_embedding = query_embedding.embeddings[0].values

similarity_scores = cosine_similarity([query_embedding], embedding)

results = sorted(zip(chunks, similarity_scores[0]), key=lambda x: x[1], reverse=True)

for i, (chunk, score) in enumerate(results[0:3]):
    print(f"Rank {i+1}:")
    print(f"Similarity Score: {score}")
    print(f"Content: {chunk.page_content}")
    print("=="*30)


######################## Questions to copy #########################################

#რამდენი ღირს ოთხი ადამიანისთვის განკუთვნილი ნომერი?
#საუზმე შედის ნომრის ფასში?
#შემიძლია თუ არა ჯავშნის გაუქმება ჩამოსვლამდე ერთი დღით ადრე?
#რომელ საათზე უნდა დავტოვო ნომერი?
#რა აქტივობებია ხელმისაწვდომი სტუმრებისთვის?
#რა პირობებია შინაური ცხოველის წამოყვანისთვის?
#რა მოხდება, თუ ჯავშნის გარეშე კი არა, დაჯავშნილი ნომრით საერთოდ არ მივალ?