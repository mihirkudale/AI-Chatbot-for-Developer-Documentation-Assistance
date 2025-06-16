from fastapi import FastAPI
from dotenv import load_dotenv
import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Ensure the index is loaded correctly.
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

@app.get("/")
async def root():
    return {"message": "Developer Documentation Chatbot is Running 🚀"}

@app.get("/query/")
async def query_docs(question: str):
    response = index.as_query_engine().query(question)
    return {"response": str(response)}

