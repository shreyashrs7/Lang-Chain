from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-2.5-flash')

prompt = PromptTemplate(
    template="Generate a summary from the {topic}",
    input_variables=['topic']
)

parser= StrOutputParser()

loader = TextLoader("langchain-document-loaders/cricket.txt")

docs = loader.load()

print(type(docs))

print(docs[0])

print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'topic': docs[0].page_content})

print("summary: \n", result)

# print(f"Result: \n{result}")

