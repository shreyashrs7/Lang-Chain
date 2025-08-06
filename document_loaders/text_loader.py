from langchain_community.document_loaders import TextLoader

loader = TextLoader("langchain-document-loaders/cricket.txt")

docs = loader.load()

print(type(docs))

print(docs[0])

print(type(docs[0]))