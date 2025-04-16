from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding  # 使用 Ollama 嵌入模型
from IPython.display import Markdown, display
import chromadb
import os
import getpass

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

from llama_index.llms.ollama import Ollama

# create client and a new collection
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

# define embedding function
embed_model = OllamaEmbedding(model_name="mistral")  # 使用本地 Ollama 嵌入模型

# load documents
documents = SimpleDirectoryReader("./data/paul_graham/").load_data()

# set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# Query Data
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))