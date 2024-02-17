from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext

#llm = Ollama(model="llama2")

#resp = llm.complete("Who is Paul Graham?")

#print(resp)
service_context = ServiceContext.from_defaults(chunk_size=1024, llm="local", embed_model="local")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is a Koi fish?")

print(response)