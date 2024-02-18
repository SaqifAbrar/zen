# Load web page
import argparse

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Embed and store
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings

from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain import hub
from langchain.chains import RetrievalQA

def zen_rag(query):    
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=GPT4AllEmbeddings())

    #print(f"Loaded {len(data)} documents")

    # RAG prompt
    
    QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")


    # LLM
    llm = Ollama(model="llama2",
                verbose=True,
                callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    print(f"Loaded LLM model {llm.model}")

    # QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True,
    )

    # Ask a question
    question = query
    result = qa_chain({"query": question})
    #source = (result["source_documents"][0].metadata)["source"]
    
    return result

