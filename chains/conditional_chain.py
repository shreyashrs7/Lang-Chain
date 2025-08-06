from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Classify the sentiment of the follwoing feedback text into positive and negative \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser

result = classifier_chain.invoke({'feedback': 'The quality is very good'})

print(result)
