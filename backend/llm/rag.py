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

def main():
    parser = argparse.ArgumentParser(description='Filter out URL argument.')
    parser.add_argument('--url', type=str, default='http://example.com', required=True, help='The URL to filter out.')

    args = parser.parse_args()
    url = args.url
    print(f"using URL: {url}")

    loader = WebBaseLoader(url)
    data = loader.load()

    # Split into chunks 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    all_splits = text_splitter.split_documents(data)
    print(f"Split into {len(all_splits)} chunks")

    vectorstore = Chroma.from_documents(documents=all_splits,
                                        embedding=GPT4AllEmbeddings(), 
                                        persist_directory="./chroma_db")
    
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=GPT4AllEmbeddings())

    #print(f"Loaded {len(data)} documents")
    url = "https://en.wikipedia.org/wiki/koi"

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
    question = f"Give me 5 fun facts about koi fish"
    result = qa_chain({"query": question})

    for x in range(len(result["source_documents"][0].metadata)):
        print(result["source_documents"][x].metadata)
    


if __name__ == "__main__":
    main()








