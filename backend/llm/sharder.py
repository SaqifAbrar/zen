# Load web page
import argparse

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Embed and store
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings


class WebStorer:
  def __init__(self, urls=['http://example.com']):
    self.urls = urls
      
  def add_url(self, url):
    self.urls.append(url)
    
  def add_urls(self, urls=[]):
    self.urls = self.urls + urls

  def store_data(self):
    for url in self.urls:
      print(url)
      loader = WebBaseLoader(url)
      data = loader.load()

      # Split into chunks 
      text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
      all_splits = text_splitter.split_documents(data)
      print(f"Split into {len(all_splits)} chunks")

      vectorstore = Chroma.from_documents(documents=all_splits,
                                          embedding=GPT4AllEmbeddings(), 
                                          persist_directory="./chroma_db")

      return vectorstore
    

urls = ['http://example.com', 'https://en.wikipedia.org/wiki/koi', 'https://www.petmd.com/fish/care/evr_fi_facts-about-koi-fish']

loader = WebStorer(urls)

loader.store_data()
