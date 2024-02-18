from langchain_community.llms import Ollama
from langchain_community.prompts import PromptTemplate
from langchain_community.chain import LLMChain

llm = Ollama(model="llama2")
print(llm.invoke("the first man on the moon was..."))

what_prompt = PromptTemplate(
  input_variables=["topic"],
  template="Give me 5 interesting facts about {topic}."
)



'''import os
os.environ["OPENAI_API_KEY"] = "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"

from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
# from IPython.display import Markdown, display

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents)

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context=storage_context)''' 